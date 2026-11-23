import test from "node:test";
import assert from "node:assert/strict";
import { add } from "../src/math.js";

test("2 + 3 应该等于 5", () => {
  assert.equal(add(2, 3), 5);
});

test("负数可以参与计算", () => {
  assert.equal(add(-1, 1), 0);
});

test("非数字参数应该抛出异常", () => {
  assert.throws(() => add("2", 3), TypeError);
});