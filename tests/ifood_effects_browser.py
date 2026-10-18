"""Event-level checks for cart celebration and order status scenes."""
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
import os, json, shutil

BASE=os.environ.get('BASE_URL','http://127.0.0.1:3000/')
OUT=Path(os.environ.get('TEST_OUTPUT','verification-local/effects'))
OUT.mkdir(parents=True,exist_ok=True)
checks=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':390,'height':844})
    page.add_init_script("sessionStorage.setItem('ifood-splash-seen','1')")
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(BASE+'#/ifood/restaurant/burger')
    page.locator('[data-action="product"][data-id="classic"]').click()
    expect(page.locator('[data-cart-celebration]')).to_have_count(0)
    page.locator('[data-action="add-cart"]').click()
    confetti=page.locator('[data-cart-celebration] [data-motion]')
    expect(confetti).to_have_attribute('data-ready','true')
    assert page.evaluate('JSON.parse(localStorage.getItem("rea-web-v1")).cart[0].qty')==1
    first=confetti.inner_html()
    page.wait_for_timeout(250)
    assert first!=confetti.inner_html(),'Confetti geometry did not animate'
    page.wait_for_timeout(300)
    page.screenshot(path=str(OUT/'cart-confetti.png'))
    assert page.locator('[data-cart-celebration]').evaluate('(e)=>getComputedStyle(e).pointerEvents')=='none'
    expect(page.locator('[data-cart-celebration]')).to_have_count(0,timeout=5000)
    checks.append('Confetti plays only after cart commit, animates, never blocks interaction and removes itself')
    # Opening another store must not celebrate until replacement is authorized.
    page.goto(BASE+'#/ifood/restaurant/pizza')
    page.locator('[data-action="product"]').first.click()
    page.locator('[data-action="add-cart"]').click()
    expect(page.get_by_role('heading',name='Começar uma nova sacola?')).to_be_visible()
    expect(page.locator('[data-cart-celebration]')).to_have_count(0)
    page.get_by_role('button',name='Manter minha sacola',exact=True).click()
    assert page.evaluate('JSON.parse(localStorage.getItem("rea-web-v1")).cartRestaurant')=='burger'
    checks.append('Declining restaurant replacement preserves the cart and does not celebrate')
    page.locator('.mobile-cart').click()
    page.locator('[data-action="checkout"]').click()
    page.locator('[data-action="place-order"]').click()
    accepted=page.locator('[data-order-motion="accepted"]')
    expect(accepted).to_be_visible()
    expect(accepted).to_have_attribute('data-playback','playing')
    page.wait_for_timeout(850)
    page.screenshot(path=str(OUT/'order-accepted.png'))
    expect(accepted).to_have_attribute('data-playback','complete',timeout=4000)
    page.reload()
    expect(page.locator('[data-order-motion="accepted"]')).to_have_attribute('data-playback','static')
    checks.append('Accepted order has its own one-shot scene and does not replay after reload')
    page.locator('[data-action="advance-order"]').click()
    preparing=page.locator('[data-order-motion="preparing"]')
    expect(page.get_by_role('heading',name='Preparando seu pedido',exact=True)).to_be_visible()
    expect(preparing).to_be_visible()
    expect(preparing).to_have_attribute('data-playback','playing')
    expect(accepted).to_have_count(0)
    assert page.evaluate('window.scrollY')==0,'Preparation status must be visible after advancing'
    page.wait_for_timeout(650)
    a=preparing.locator('.prep-lid').evaluate('(e)=>getComputedStyle(e).transform')
    steam=preparing.locator('.steam-two').evaluate('(e)=>getComputedStyle(e).transform')
    page.wait_for_timeout(220)
    assert a!=preparing.locator('.prep-lid').evaluate('(e)=>getComputedStyle(e).transform'),'Lid did not animate'
    assert steam!=preparing.locator('.steam-two').evaluate('(e)=>getComputedStyle(e).transform'),'Steam did not animate'
    page.screenshot(path=str(OUT/'preparing-order.png'))
    expect(preparing).to_have_attribute('data-playback','complete',timeout=5000)
    for width in [360,390,1440]:
        page.set_viewport_size({'width':width,'height':844})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        page.screenshot(path=str(OUT/f'preparing-{width}.png'))
    page.set_viewport_size({'width':390,'height':844})
    page.reload()
    expect(preparing).to_have_attribute('data-playback','static')
    assert preparing.evaluate('(e)=>e.getAnimations({subtree:true}).length')==0
    checks.append('Preparing animates its pot lid and steam once, remains responsive and does not replay after reload')
    saved_order=page.evaluate('localStorage.getItem("rea-web-v1")')
    for preference in ['reduce','no-preference']:
        accessible=browser.new_page(viewport={'width':390,'height':844},reduced_motion=preference)
        accessible.on('pageerror',lambda e:errors.append(str(e)))
        accessible.add_init_script('localStorage.setItem("rea-web-v1",'+json.dumps(saved_order)+');sessionStorage.setItem("ifood-splash-seen","1")')
        accessible.goto(page.url)
        scene=accessible.locator('[data-order-motion="preparing"]')
        expect(scene).to_be_visible()
        if preference=='no-preference':
            expect(scene).to_have_attribute('data-playback','playing')
            accessible.emulate_media(reduced_motion='reduce')
        expect(scene).to_have_attribute('data-playback','static')
        assert scene.evaluate('(e)=>e.getAnimations({subtree:true}).length')==0
        expect(accessible.get_by_role('heading',name='Preparando seu pedido',exact=True)).to_be_visible()
        accessible.close()
    checks.append('Preparation is static for reduced motion, including when the preference changes during playback')
    page.locator('[data-action="advance-order"]').click()
    expect(preparing).to_have_count(0)
    rider=page.locator('[data-order-motion="delivery"]')
    expect(rider).to_be_visible()
    expect(rider).to_have_attribute('data-playback','playing')
    assert page.evaluate('window.scrollY')==0, 'Delivery status must be visible after advancing the demo'
    expect(rider.locator('img')).to_have_attribute('alt','Entregador de moto com mochila vermelha')
    page.wait_for_timeout(600)
    a=rider.locator('.courier-rider').evaluate('(e)=>getComputedStyle(e).transform')
    page.wait_for_timeout(200)
    b=rider.locator('.courier-rider').evaluate('(e)=>getComputedStyle(e).transform')
    assert a!=b,'Courier did not animate'
    page.screenshot(path=str(OUT/'out-for-delivery.png'))
    page.emulate_media(reduced_motion='reduce')
    expect(rider).to_have_attribute('data-playback','static')
    assert rider.evaluate('(e)=>e.getAnimations({subtree:true}).every(a=>a.playState!=="running")')
    page.emulate_media(reduced_motion='no-preference')
    page.locator('[data-action="advance-order"]').click()
    expect(page.locator('[data-order-motion="delivery"]')).to_have_count(0)
    checks.append('Delivery uses the researched rider, moves, stops for reduced motion and disappears on completion')
    delivered=page.locator('[data-order-motion="delivered"]')
    expect(delivered).to_be_visible()
    expect(delivered).to_have_attribute('data-playback','playing')
    expect(page.get_by_role('heading',name='Pedido entregue',exact=True)).to_be_visible()
    expect(page.locator('[data-action="advance-order"]')).to_have_count(0)
    expect(page.locator('.order-loader')).to_have_count(0)
    assert page.evaluate('window.scrollY')==0,'Delivered status must be visible after advancing'
    page.wait_for_timeout(100)
    a=delivered.locator('.delivered-bag').evaluate('(e)=>getComputedStyle(e).transform')
    page.wait_for_timeout(220)
    assert a!=delivered.locator('.delivered-bag').evaluate('(e)=>getComputedStyle(e).transform'),'Delivered bag did not animate'
    page.wait_for_timeout(500)
    assert delivered.locator('.delivered-confetti').evaluate_all('(els)=>els.some(e=>Number(getComputedStyle(e).opacity)>0)'), 'Delivery celebration did not appear'
    page.screenshot(path=str(OUT/'order-delivered.png'))
    expect(delivered).to_have_attribute('data-playback','complete',timeout=4000)
    # Chromium may retain rounding residuals (e.g. 4e-16) after commitStyles.
    assert delivered.locator('.delivered-confetti').evaluate_all('(els)=>els.every(e=>Number(getComputedStyle(e).opacity)<0.001)')
    page.reload()
    expect(delivered).to_have_attribute('data-playback','static')
    assert delivered.evaluate('(e)=>e.getAnimations({subtree:true}).length')==0
    for width in [360,390,1440]:
        page.set_viewport_size({'width':width,'height':844})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        page.screenshot(path=str(OUT/f'delivered-{width}.png'))
    page.set_viewport_size({'width':390,'height':844})
    checks.append('Delivered order animates bag and celebration once, stops, remains responsive and stays static after reload')
    saved_order=page.evaluate('localStorage.getItem("rea-web-v1")')
    for preference in ['reduce','no-preference']:
        accessible=browser.new_page(viewport={'width':390,'height':844},reduced_motion=preference)
        accessible.on('pageerror',lambda e:errors.append(str(e)))
        accessible.add_init_script('localStorage.setItem("rea-web-v1",'+json.dumps(saved_order)+');sessionStorage.setItem("ifood-splash-seen","1")')
        accessible.goto(page.url)
        scene=accessible.locator('[data-order-motion="delivered"]')
        expect(scene).to_be_visible()
        if preference=='no-preference':
            expect(scene).to_have_attribute('data-playback','playing')
            accessible.emulate_media(reduced_motion='reduce')
        expect(scene).to_have_attribute('data-playback','static')
        assert scene.evaluate('(e)=>e.getAnimations({subtree:true}).length')==0
        expect(accessible.get_by_role('heading',name='Pedido entregue',exact=True)).to_be_visible()
        accessible.close()
    checks.append('Delivered scene respects reduced motion before playback and when the preference changes')
    page.emulate_media(reduced_motion='reduce')
    page.goto(BASE+'#/ifood/restaurant/burger')
    page.locator('[data-action="product"]').first.click()
    page.locator('[data-action="add-cart"]').click()
    expect(page.locator('#toast')).to_contain_text('Adicionado')
    expect(page.locator('[data-cart-celebration]')).to_have_count(0)
    checks.append('Reduced motion retains cart confirmation without confetti')
    for width in [360,390,1440]:
        page.set_viewport_size({'width':width,'height':844})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not errors,errors
    (OUT/'effects-results.json').write_text(json.dumps({'passed':checks,'runtime_errors':errors},ensure_ascii=False,indent=2))
    print('\n'.join('PASS '+c for c in checks))
    browser.close()
