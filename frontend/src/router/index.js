import Vue from "vue";
import Router from "vue-router";
import TopPage from "@/components/TopPage";
import Register from "@/components/Register";
import Generate from "@/components/Generate";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "top",
      component: TopPage
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/generate",
      name: "generatere",
      component: Generate
    }
  ]
});
