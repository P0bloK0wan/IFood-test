// Order scenes are web adaptations. Cart confetti preserves the recovered
// campaign's selected layers/keyframes; see assets/effects/manifest.json.
import { mountMotion } from "./motion.js";

const reduced = matchMedia("(prefers-reduced-motion: reduce)");
const scenes = new Map();
const seen = new Set();
let celebration = null;
try {
  const saved = JSON.parse(
    sessionStorage.getItem("ifood-order-motion-seen") || "[]",
  );
  if (Array.isArray(saved)) saved.slice(-80).forEach((key) => seen.add(key));
} catch {
  /* Session storage is optional; cart/order persistence is separate. */
}

function remember(key) {
  seen.add(key);
  while (seen.size > 80) seen.delete(seen.values().next().value);
  try {
    sessionStorage.setItem(
      "ifood-order-motion-seen",
      JSON.stringify([...seen]),
    );
  } catch {
    /* A denied session store must not interrupt checkout. */
  }
}

export function orderScene(order) {
  const id = String(order.id).replace(/[^a-zA-Z0-9_-]/g, "");
  if (order.status === "confirmed") {
    return `<div class="order-scene acceptance-scene" data-order-motion="accepted" data-order-id="${id}" aria-hidden="true">
      <div class="accept-halo"></div><div class="accept-shadow"></div>
      <div class="accept-bag"><span class="accept-handle"></span><img src="./assets/identity/ifood/logo.svg" alt=""></div>
      <span class="accept-spark spark-one">✦</span><span class="accept-spark spark-two">✦</span><span class="accept-spark spark-three"></span>
      <span class="accept-check"><svg viewBox="0 0 40 40"><path d="m10 21 7 7 14-15" pathLength="1"/></svg></span>
    </div>`;
  }
  if (order.status === "preparing") {
    return `<div class="order-scene preparation-scene" data-order-motion="preparing" data-order-id="${id}" aria-hidden="true">
      <div class="prep-halo"></div><div class="prep-shadow"></div>
      <svg class="prep-steam" viewBox="0 0 104 66"><path class="steam-one" d="M22 56c-14-12 14-16 0-30"/><path class="steam-two" d="M52 48c-17-14 17-19 0-35"/><path class="steam-three" d="M82 56c-14-12 14-16 0-30"/></svg>
      <div class="prep-pot"><span class="prep-handle handle-left"></span><span class="prep-handle handle-right"></span><div class="prep-body"><img src="./assets/identity/ifood/logo.svg" alt=""></div><div class="prep-lid"><span></span></div></div>
    </div>`;
  }
  if (order.status === "delivering") {
    return `<div class="order-scene delivery-scene" data-order-motion="delivery" data-order-id="${id}">
      <div class="courier-sky" aria-hidden="true"></div>
      <svg class="courier-city" viewBox="0 0 360 130" aria-hidden="true"><path d="M0 113H29V61H68V113H88V38H117V113H138V74H167V113H195V48H226V113H253V24H283V113H305V67H340V113H360"/><path d="M39 73h5m10 0h5M39 90h5m10 0h5M97 54h9m-9 17h9m-9 17h9M263 42h10m-10 18h10m-10 18h10M315 82h14m-14 17h14"/></svg>
      <span class="courier-speed speed-one" aria-hidden="true"></span><span class="courier-speed speed-two" aria-hidden="true"></span>
      <div class="courier-entry"><img class="courier-rider" src="./assets/effects/ifood/courier.png" alt="Entregador de moto com mochila vermelha"></div>
      <div class="courier-road" aria-hidden="true"><span></span></div>
    </div>`;
  }
  if (order.status === "completed") {
    return `<div class="order-scene completed-scene" data-order-motion="delivered" data-order-id="${id}" aria-hidden="true">
      <div class="delivered-halo"></div><div class="delivered-ring"></div><div class="delivered-shadow"></div>
      <div class="accept-bag delivered-bag"><span class="accept-handle"></span><img src="./assets/identity/ifood/logo.svg" alt=""></div>
      <span class="accept-check delivered-check"><svg viewBox="0 0 40 40"><path d="m10 21 7 7 14-15" pathLength="1"/></svg></span>
      <span class="delivered-spark">✦</span><span class="delivered-spark small">✦</span>
      ${Array.from({ length: 8 }, () => '<i class="delivered-confetti"></i>').join("")}
    </div>`;
  }
  return "";
}

function finishScene(el, record, state = "complete") {
  if (!record || record.finished) return;
  record.finished = true;
  record.animations.forEach((animation) => {
    if (state === "complete" && el.isConnected) {
      try {
        animation.commitStyles();
      } catch {
        /* Detached targets need no retained styles. */
      }
    }
    animation.cancel();
  });
  if (el.isConnected) el.dataset.playback = state;
}

export function mountOrderScenes(root = document) {
  for (const el of root.querySelectorAll("[data-order-motion]")) {
    if (scenes.has(el)) continue;
    const record = { animations: [], finished: false };
    scenes.set(el, record);
    const key = el.dataset.orderId + ":" + el.dataset.orderMotion;
    if (reduced.matches || seen.has(key)) {
      el.dataset.playback = "static";
      record.finished = true;
      remember(key);
      continue;
    }
    remember(key);
    el.dataset.playback = "playing";
    const animate = (selector, frames, timing) => {
      const target = el.querySelector(selector);
      if (target) record.animations.push(target.animate(frames, timing));
    };
    if (el.dataset.orderMotion === "accepted") {
      animate(
        ".accept-bag",
        [
          {
            transform: "translateY(24px) rotate(-7deg) scale(.82)",
            opacity: 0,
          },
          {
            transform: "translateY(-5px) rotate(2deg) scale(1.03)",
            opacity: 1,
            offset: 0.7,
          },
          { transform: "translateY(0) rotate(0) scale(1)", opacity: 1 },
        ],
        { duration: 720, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      animate(
        ".accept-halo",
        [
          { transform: "scale(.55)", opacity: 0 },
          { transform: "scale(1.08)", opacity: 1, offset: 0.55 },
          { transform: "scale(1)", opacity: 1 },
        ],
        { duration: 1150 },
      );
      animate(
        ".accept-shadow",
        [
          { transform: "scale(.55)", opacity: 0 },
          { transform: "scale(1)", opacity: 1 },
        ],
        { duration: 720 },
      );
      animate(
        ".accept-check",
        [
          { transform: "scale(0)", opacity: 0 },
          { transform: "scale(1.12)", opacity: 1, offset: 0.7 },
          { transform: "scale(1)", opacity: 1 },
        ],
        { delay: 350, duration: 500, fill: "backwards" },
      );
      animate(
        ".accept-check path",
        [{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }],
        { delay: 600, duration: 380, fill: "backwards", easing: "ease-out" },
      );
      for (const [i, name] of [
        ".spark-one",
        ".spark-two",
        ".spark-three",
      ].entries()) {
        animate(
          name,
          [
            { transform: "translateY(8px) scale(0)", opacity: 0 },
            {
              transform: "translateY(-3px) scale(1.2)",
              opacity: 1,
              offset: 0.5,
            },
            { transform: "translateY(0) scale(1)", opacity: 1 },
          ],
          { delay: 300 + i * 90, duration: 700, fill: "backwards" },
        );
      }
    } else if (el.dataset.orderMotion === "preparing") {
      animate(
        ".prep-pot",
        [
          { transform: "translateY(18px) scale(.9)", opacity: 0 },
          {
            transform: "translateY(-3px) scale(1.02)",
            opacity: 1,
            offset: 0.7,
          },
          { transform: "translateY(0) scale(1)", opacity: 1 },
        ],
        { duration: 650, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      animate(
        ".prep-halo",
        [
          { transform: "scale(.8)", opacity: 0 },
          { transform: "scale(1)", opacity: 1 },
        ],
        { duration: 800, easing: "ease-out" },
      );
      animate(
        ".prep-shadow",
        [
          { transform: "scale(.75)", opacity: 0 },
          { transform: "scale(1)", opacity: 0.65 },
        ],
        { duration: 650, easing: "ease-out" },
      );
      animate(
        ".prep-lid",
        [
          { transform: "translateY(0) rotate(0)" },
          { transform: "translateY(-7px) rotate(-3deg)", offset: 0.35 },
          { transform: "translateY(-4px) rotate(2deg)", offset: 0.65 },
          { transform: "translateY(0) rotate(0)" },
        ],
        { duration: 1400, iterations: 3, delay: 250, easing: "ease-in-out" },
      );
      for (const [i, name] of [
        ".steam-one",
        ".steam-two",
        ".steam-three",
      ].entries()) {
        animate(
          name,
          [
            { transform: "translateY(6px) scaleX(.85)", opacity: 0.15 },
            {
              transform: "translateY(-3px) scaleX(1.1)",
              opacity: 0.8,
              offset: 0.55,
            },
            { transform: "translateY(0) scaleX(1)", opacity: 0.65 },
          ],
          {
            duration: 1400,
            iterations: 3,
            delay: i * 160,
            easing: "ease-in-out",
          },
        );
      }
    } else if (el.dataset.orderMotion === "delivered") {
      animate(
        ".delivered-bag",
        [
          {
            transform: "translate(-40px,-12px) rotate(-9deg) scale(.9)",
            opacity: 0,
          },
          {
            transform: "translate(2px,3px) rotate(2deg) scale(1.02)",
            opacity: 1,
            offset: 0.72,
          },
          { transform: "translate(0,0) rotate(0) scale(1)", opacity: 1 },
        ],
        { duration: 800, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      animate(
        ".delivered-halo",
        [
          { transform: "scale(.65)", opacity: 0 },
          { transform: "scale(1)", opacity: 1 },
        ],
        { duration: 850, easing: "ease-out" },
      );
      animate(
        ".delivered-shadow",
        [
          { transform: "scale(.6)", opacity: 0 },
          { transform: "scale(1)", opacity: 0.65 },
        ],
        { duration: 800 },
      );
      animate(
        ".delivered-check",
        [
          { transform: "scale(0) rotate(-15deg)", opacity: 0 },
          { transform: "scale(1.12) rotate(3deg)", opacity: 1, offset: 0.7 },
          { transform: "scale(1) rotate(0)", opacity: 1 },
        ],
        { duration: 550, delay: 400, fill: "backwards" },
      );
      animate(
        ".delivered-check path",
        [{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }],
        { duration: 380, delay: 750, fill: "backwards", easing: "ease-out" },
      );
      animate(
        ".delivered-ring",
        [
          { transform: "scale(.55)", opacity: 0 },
          { transform: "scale(.9)", opacity: 0.7, offset: 0.3 },
          { transform: "scale(1.2)", opacity: 0 },
        ],
        { duration: 1200, delay: 350, fill: "backwards", easing: "ease-out" },
      );
      const bursts = [
        [-86, -38, -70],
        [-55, -64, 35],
        [-13, -72, -35],
        [45, -66, 80],
        [84, -34, -45],
        [91, 10, 60],
        [-82, 19, 45],
        [60, 35, -70],
      ];
      el.querySelectorAll(".delivered-confetti").forEach((target, i) => {
        const [x, y, rotation] = bursts[i];
        record.animations.push(
          target.animate(
            [
              { transform: "translate(0,8px) rotate(0) scale(0)", opacity: 0 },
              {
                transform: `translate(${x * 0.8}px,${y}px) rotate(${rotation}deg) scale(1)`,
                opacity: 1,
                offset: 0.45,
              },
              {
                transform: `translate(${x}px,${y + 24}px) rotate(${rotation * 2}deg) scale(.75)`,
                opacity: 0,
              },
            ],
            {
              duration: 900,
              delay: 500 + i * 35,
              easing: "ease-out",
              fill: "backwards",
            },
          ),
        );
      });
    } else {
      animate(
        ".courier-entry",
        [
          { transform: "translateX(-110px)", opacity: 0 },
          { transform: "translateX(0)", opacity: 1 },
        ],
        { duration: 800, easing: "cubic-bezier(.16,1,.3,1)" },
      );
      animate(
        ".courier-rider",
        [
          { transform: "translateY(0) rotate(-.3deg)" },
          { transform: "translateY(-2px) rotate(.3deg)", offset: 0.5 },
          { transform: "translateY(0) rotate(-.3deg)" },
        ],
        { duration: 600, iterations: 8, easing: "ease-in-out" },
      );
      animate(
        ".courier-road span",
        [{ transform: "translateX(0)" }, { transform: "translateX(-72px)" }],
        { duration: 600, iterations: 8, easing: "linear" },
      );
      animate(
        ".courier-city",
        [{ transform: "translateX(15px)" }, { transform: "translateX(-15px)" }],
        { duration: 4800, easing: "linear" },
      );
      for (const [i, name] of [".speed-one", ".speed-two"].entries()) {
        animate(
          name,
          [
            { transform: "translateX(15px) scaleX(.4)", opacity: 0 },
            { transform: "translateX(0) scaleX(1)", opacity: 1, offset: 0.4 },
            { transform: "translateX(-35px) scaleX(.7)", opacity: 0 },
          ],
          { duration: 800, iterations: 5, delay: i * 160 },
        );
      }
    }
    Promise.allSettled(record.animations.map((a) => a.finished)).then(() =>
      finishScene(el, record),
    );
  }
}

export function clearCartCelebration() {
  if (!celebration) return;
  clearTimeout(celebration.timeout);
  celebration.pulse?.cancel();
  celebration.el.remove();
  celebration = null;
}

export function celebrateCart() {
  clearCartCelebration();
  if (
    reduced.matches ||
    document.hidden ||
    document.body.dataset.app !== "ifood"
  )
    return;
  const el = document.createElement("div");
  el.className = "cart-celebration";
  el.dataset.cartCelebration = "true";
  el.setAttribute("aria-hidden", "true");
  el.innerHTML =
    '<span class="native-motion" data-motion="./assets/effects/ifood/cart-confetti.json" data-loop="false"></span>';
  document.body.append(el);
  const cart = [...document.querySelectorAll('[data-action="cart"]')].find(
    (node) => node.offsetWidth,
  );
  const record = { el, timeout: null, pulse: null };
  celebration = record;
  const cleanup = () => {
    if (celebration === record) clearCartCelebration();
  };
  el.firstElementChild.addEventListener("motion-complete", cleanup, {
    once: true,
  });
  el.firstElementChild.addEventListener("motion-failed", cleanup, {
    once: true,
  });
  record.timeout = setTimeout(cleanup, 5000);
  record.pulse = cart?.animate(
    [
      { transform: "scale(1)" },
      { transform: "scale(1.025)", offset: 0.45 },
      { transform: "scale(1)" },
    ],
    { duration: 420, delay: 180, easing: "ease-out" },
  );
  mountMotion(el);
}

new MutationObserver(() => {
  for (const [el, record] of scenes) {
    if (!el.isConnected) {
      finishScene(el, record);
      scenes.delete(el);
    }
  }
}).observe(document.documentElement, { childList: true, subtree: true });
reduced.addEventListener("change", () => {
  if (!reduced.matches) return;
  clearCartCelebration();
  for (const [el, record] of scenes) finishScene(el, record, "static");
});
document.addEventListener("visibilitychange", () => {
  if (document.hidden) clearCartCelebration();
  for (const record of scenes.values()) {
    if (!record.finished)
      record.animations.forEach((a) =>
        document.hidden ? a.pause() : a.play(),
      );
  }
});
window.addEventListener("hashchange", clearCartCelebration);
