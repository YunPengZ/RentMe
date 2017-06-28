import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'

Vue.use(Router)

import NotFound from '../components/NotFound.vue'
import Hello from '../components/Hello.vue'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Navbar from '../components/Navbar.vue'
import Welcome from '../components/Welcome.vue'
import Order from '../components/Order.vue'
import NewOrder from '../components/NewOrder.vue'
import UserInfo from '../components/UserInfo.vue'
import CarModel from '../components/CarModel.vue'
import violationInfo from '../components/violation_info.vue'
import CarManage from '../components/carManage.vue'
import OrderCharge from '../components/OrderCharge.vue'
import editCar from '../components/editCar.vue'
import addCar from '../components/addCar.vue'
import storeManage from '../components/storeManage.vue'
import addStore from '../components/addStore.vue'
import editStore from '../components/editStore.vue'
import addManager from '../components/addManager.vue'
import editManager from '../components/editManager.vue'
import Analysis from '../components/Analysis.vue'

const router = new Router({
  routes: [
    {
      path: '*',
      name: '404',
      component: NotFound
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      components: {
        top: Navbar,
        default: Home
      },
      children: [
        {path: '', component: Welcome},
        {path: 'order', component: Order},
        {path: 'new_order',
          component: NewOrder,
          children: [
            {path: '', component: UserInfo},
            {path: 'car_model', component: CarModel},
            {path: 'order_charge', component: OrderCharge}
          ]
        },
        {path: 'carManage', component: CarManage},
        {path: 'storeManage', component: storeManage},
        {path: 'editCar', component: editCar},
        {path: 'addCar', component: addCar},
        {path: 'addStore', component: addStore},
        {path: 'editStore', component: editStore},
        {path: 'addManager', component: addManager},
        {path: 'editManager', component: editManager},
        {path: 'violation_info', component: violationInfo},
        {path: 'Analysis', component: Analysis}
      ]
    },
    {
      path: '/hello',
      component: Hello,
      meta: { requiresAuth: true }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (store.state.user_ID.length === 0) {
      next({
        path: '/login',
        query: { redirect: to.path }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

export default router
