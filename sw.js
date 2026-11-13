// Service worker: nätverk först (uppdateringar vinner), cache som offline-reserv
const CACHE = 'sagsand-v3'; // v3: rensar bort gamla versionskoller som hamnat i cachen
const ASSETS = ['./', './index.html', './manifest.json',
  './icons/icon-192.png', './icons/icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ).then(() => self.clients.claim()));
});
// Sidan kan be den väntande workern ta över direkt
self.addEventListener('message', (e) => {
  if (e.data && e.data.type === 'SKIP_WAITING') self.skipWaiting();
});
self.addEventListener('fetch', (e) => {
  // Versionskollen (cache: 'no-store') och allt som inte är GET ska gå direkt mot nätet
  // och aldrig sparas — annars växer cachen med en post per minut.
  if (e.request.cache === 'no-store' || e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request).then(resp => {
      const copy = resp.clone();
      caches.open(CACHE).then(c => c.put(e.request, copy)).catch(()=>{});
      return resp;
    }).catch(() => caches.match(e.request))
  );
});
