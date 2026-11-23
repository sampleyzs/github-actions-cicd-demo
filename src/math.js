export function add(a, b) {
  if (!Number.isFinite(a) || !Number.isFinite(b)) {
    throw new TypeError("两个参数都必须是有效数字");
  }

  return a + b;
}