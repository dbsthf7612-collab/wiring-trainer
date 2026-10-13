// app.html(본문만 있는 파일) → index.html(완전한 웹페이지). GitHub Pages는 index.html을 보여줌
// 사용법: node build.js
const fs = require('fs');
const body = fs.readFileSync(__dirname + '/app.html', 'utf8');
const split = body.indexOf('<div class="wrap">');
const head = body.slice(0, split).trim();   // <title>, 폰트, <style>
const main = body.slice(split).trim();      // 화면 + <script>

const html = `<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="시퀀스 도면을 보고 가상 판넬에 배선해 보는 연습 게임. 기초부터 전기기능사 실기 수준까지.">
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="배선 연습">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#1d262b">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}</style>
${head}
</head>
<body>
${main}
<script>if('serviceWorker' in navigator)navigator.serviceWorker.register('sw.js').catch(()=>{});</script>
</body>
</html>
`;
fs.writeFileSync(__dirname + '/index.html', html);
console.log('index.html 생성 완료');
