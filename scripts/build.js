import { cp, mkdir, rm } from "node:fs/promises";

await rm("dist", { recursive: true, force: true });
await mkdir("dist", { recursive: true });

await cp("index.html", "dist/index.html");
await cp("src", "dist/src", { recursive: true });

console.log("构建完成，网页文件位于 dist 目录");