<template>
  <div>
    <el-row>
      <el-col :span="6">
        <el-form :model="form" label-width="100px">
          <el-form-item label="手机号">
            <el-input v-model="form.account" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="form.password" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">提交</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
      data () {
        return {
          form: {
            account: '',
            password: ''
          }
        }
      },
  methods: {
        login () {
          var self = this
          console.log(self.form.account)
          axios.post('/test/login/?format=json', {
            admin_tel: self.form.account,
            admin_pas: self.form.password
          })
            .then(function (response) {
              console.log('1233')
            // console.log(response.data[0])
            // self.$store.commit('changeUser',response.data[0]) //改变选中的用户的姓名，值，以便寻找比赛
            // $router.go({name: 'register', params: {id:'apply'}})
            // console.log(self.$router.path)
            })
            .catch(e => {
              self.$message('账号或者密码错误，请重新输入')
              this.errors.push(e)
            })
        }
  }

    }
</script>

<style scoped>

</style>
