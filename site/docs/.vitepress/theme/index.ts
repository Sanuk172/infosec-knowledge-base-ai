import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import "./custom.css";
import AiChat from "./AiChat.vue";

const theme: Theme = {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("AiChat", AiChat);
  }
};

export default theme;
