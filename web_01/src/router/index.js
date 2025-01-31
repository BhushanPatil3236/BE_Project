import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AuthView from '../views/AuthView.vue'
import Signin from '../components/auth/sign_in.vue'
import Signup from '../components/auth/sign_up.vue'
import ForgotPassword from '../components/auth/forgot_password.vue'
import ChangePassword from '../components/auth/change_password.vue'
import ResetPassword from '../components/auth/reset_password.vue'
import MyAccount from '../views/MyAccount.vue'
import FormData from '../views/FormView.vue'
import DataView from '../views/DataView.vue'
import Estimator from '../components/food-estimation/calorie-estimation.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: "/form",
    name: "Food-Nutrition",
    component: FormData,
  },
  {
    path: "/estimator",
    name: "Calorie-Estimator",
    component: Estimator,
  },
  {
    path: "/data",
    name: "Data",
    component: DataView,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/account',
    name: 'My Account',
    component: MyAccount
  },
  {
    path: "/auth",
    name: "Auth",
    component: AuthView,
    children: [
      {
        path: "",
        name: "Signin",
        component: Signin
      },
      {
        path: "signup",
        name: "Signup",
        component: Signup
      },
      {
        path: "forgot-password",
        name: "Forgot Password",
        component: ForgotPassword
      },
      {
        path: "change-password",
        name: "Change Password",
        component: ChangePassword
      },
      {
        path: "reset-password/:uid/:token",
        name: "Reset Password",
        component: ResetPassword
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
