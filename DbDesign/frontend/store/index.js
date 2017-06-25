import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// root state object.
// each Vuex instance is just a single state tree.
const state = {
  user_ID: '',
        // 用户ID
  user_Name: '',
        // 用户姓名
  user_Status: ''
            // 管理员等级
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
