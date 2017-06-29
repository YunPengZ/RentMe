import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// root state object.
// each Vuex instance is just a single state tree.
const state = {
  // 跟踪新订单的状态
  // 新订单目前在第几步
  step: '',
  // 该订单绑定的用户和驾驶员ID(第一步时完成)
  order_user_id: '',
  order_drive_id: '',
  // 符合所选车型的车辆ID(第二步时完成)
  matched_car: [],
  // 该订单所绑定的车辆ID(第三步时完成)
  car_ID: '',
  // 管理员ID
  user_ID: '',
  // 管理员姓名
  user_Name: '朱云鹏',
  // 管理员等级
  user_Status: '门店管理员'
}
    // mutations are operations that actually mutates the state.
    // each mutation handler gets the entire state tree as the
    // first argument, followed by additional payload arguments.
    // mutations must be synchronous and can be recorded by plugins
    // for debugging purposes.
const mutations = {
    // changeId(state, message) {
    //     state.match_ID = message
    // },
    // changeUser(state, message) {
    //     state.user_Name = message.user_Name
    //     state.user_Status = message.user_Status
    //     state.user_ID = message.user_ID
    // },
    // signOutUser(state) {
    //     state.user_Name = ''
    //     state.user_Status = 'user'
    //     state.user_ID = ''
    // },
    // changeUserName(state, message) {
    //     state.user_Name = message
    // }
}

// actions are functions that causes side effects and can involve
// asynchronous operations.
const actions = {
    // selectMatch ({ commit }, message) {
    //   commit('changeId', { id: message })
    // }
}

// getters are functions
const getters = {
    // evenOrOdd: state => state.count % 2 === 0 ? 'even' : 'odd'
}

// A Vuex instance is created by combining the state, mutations, actions,
// and getters.
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
