import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";

const entries = JSON.parse(
  readFileSync(
    new URL("../dist/assets/effects/manifest.json", import.meta.url),
  ),
);
test("courier and adapted confetti retain documented source bytes", () => {
  for (const entry of entries) {
    const bytes = readFileSync(
      new URL("../dist/" + entry.path, import.meta.url),
    );
    assert.equal(
      createHash("sha256").update(bytes).digest("hex"),
      entry.sha256,
    );
    assert.equal(bytes.length, entry.bytes);
  }
});
test("cart confetti preserves original layer transforms, keyframes and dependencies", () => {
  const entry = entries.find((e) => e.path.endsWith("cart-confetti.json"));
  const candidates = ["../", "../../"].map(
    (prefix) => new URL(prefix + entry.source, import.meta.url),
  );
  const sourceBytes = readFileSync(candidates.find((path) => existsSync(path)));
  assert.equal(
    createHash("sha256").update(sourceBytes).digest("hex"),
    entry.source_json_sha256,
  );
  const source = JSON.parse(sourceBytes);
  const adapted = JSON.parse(
    readFileSync(new URL("../dist/" + entry.path, import.meta.url)),
  );
  assert.deepEqual(
    adapted.layers,
    source.layers.filter((layer) => entry.layers.includes(layer.nm)),
  );
  for (const asset of adapted.assets)
    assert.deepEqual(
      asset,
      source.assets.find((original) => original.id === asset.id),
    );
  assert.equal(adapted.fr, source.fr);
  assert.equal(adapted.ip, entry.start);
  assert.equal(adapted.op, entry.end);
  assert.ok(adapted.ip >= source.ip && adapted.op <= source.op);
  assert.equal(adapted.w, source.w);
  assert.equal(adapted.h, source.h);
  assert.ok(
    adapted.assets.every((asset) => !asset.p),
    "Confetti should not need the campaign raster art",
  );
});
