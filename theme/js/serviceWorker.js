"use strict";

if ("serviceWorker" in navigator) {
  window.addEventListener("load", function() {
    navigator.serviceWorker
      .register("/sw.js", { scope: "/" })
      .catch(function(e) {
        console.error("Error during service worker registration:", e);
      });
  });
}
