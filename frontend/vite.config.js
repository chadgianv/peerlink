import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Forward same-origin /api calls to FastAPI during local development.
// This avoids localhost vs 127.0.0.1 CORS/origin issues.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: { "/api": { target: "http://127.0.0.1:8000", changeOrigin: true } }
  }
});
