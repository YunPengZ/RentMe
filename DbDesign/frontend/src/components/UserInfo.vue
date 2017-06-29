<template>
  <div>
    <el-row>
      <el-card>
        <h3>填写驾驶员信息</h3>
        <el-col :span="12">
          <el-form :model="form" :rules="rules" ref="form" label-width="100px">
            <el-form-item prop="checkPass">
              <el-input v-model="form.drive_name" auto-complete="off">
                <template slot="prepend">姓名</template>
              </el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
              <el-input v-model="form.user_drive" auto-complete="off">
                <template slot="prepend">驾驶证号</template>
              </el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
              <el-input v-model="form.drive_type" auto-complete="off">
                <template slot="prepend">驾驶证类型</template>
              </el-input>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="12">
          <el-form :model="form" :rules="rules" ref="form" label-width="100px">
            <el-form-item prop="checkPass">
              <el-input v-model="form.drive_age" auto-complete="off" class="input">
                <template slot="prepend">驾龄</template>
              </el-input>
            </el-form-item>
            <el-form-item prop="form">
              <el-date-picker
                v-model="form.drive_start_date"
                type="date"
                placeholder="选择发证日期">
              </el-date-picker>
            </el-form-item>
            <el-form-item prop="form">
              <el-date-picker
                v-model="form.drive_end_date"
                type="date"
                placeholder="选择失效日期">
              </el-date-picker>
            </el-form-item>
          </el-form>
        </el-col>
      </el-card>
    </el-row>
    <el-row class="row">
      <el-card>
        <h3>填写用户信息</h3>
        <el-col :span="12">
        <el-form :model="form" :rules="rules" ref="form" label-width="100px">
          <el-form-item prop="name">
            <el-input v-model="form.user_name" auto-complete="off">
              <template slot="prepend">姓名</template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <span>性别：</span>
            <el-radio class="radio" v-model="form.user_sex" label="男">男</el-radio>
            <el-radio class="radio" v-model="form.user_sex" label="女">女</el-radio>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="form.user_age">
              <template slot="prepend">年龄</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="form.user_tel">
              <template slot="prepend">电话</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="form.user_ident">
              <template slot="prepend">身份证号</template>
            </el-input>
          </el-form-item>
        </el-form>
        </el-col>
        <el-col :span="12">
          <el-form :model="form" :rules="rules" ref="form" label-width="100px">
          <el-form-item prop="pass">
            <el-input v-model="form.user_addr" auto-complete="off">
              <template slot="prepend">地址</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="checkPass">
            <el-input v-model="form.user_post" auto-complete="off">
              <template slot="prepend">邮编</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="form.user_email">
              <template slot="prepend">Email</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="form.user_office">
              <template slot="prepend">工作单位</template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm()">提交</el-button>
          </el-form-item>
        </el-form>
        </el-col>
      </el-card>
    </el-row>
  </div> 
</template>
<script>
import axios from 'axios'
export default{
  data () {
    // var checkAge = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('年龄不能为空'))
    //   }
    // }
    // var validatePass = (rule, value, callback) => {
    //   if (value === '') {
    //     callback(new Error('请输入密码'))
    //   } else {
    //     if (this.ruleForm2.checkPass !== '') {
    //       this.$refs.ruleForm2.validateField('checkPass')
    //     }
    //     callback()
    //   }
    // }
    // var validatePass2 = (rule, value, callback) => {
    //   if (value === '') {
    //     callback(new Error('请再次输入密码'))
    //   } else if (value !== this.ruleForm2.pass) {
    //     callback(new Error('两次输入密码不一致!'))
    //   } else {
    //     callback()
    //   }
    // }
    return {
      form: {
        drive_name: null,
        user_drive: null,
        drive_type: null,
        drive_age: null,
        drive_start_date: null,
        drive_end_date: null,
        user_name: null,
        user_sex: null,
        user_age: null,
        user_ident: null,
        user_tel: null,
        user_office: null,
        user_addr: null,
        user_post: null,
        user_email: null
      },
      rules: {
      }
    }
  },
  methods: {
    submitForm (formName) {
      var self = this.form
      axios.post('/test/order/create', {
        drive_name: self.drive_name,
        user_drive: self.user_drive,
        drive_type: self.drive_type,
        drive_age: self.drive_age,
        drive_start_date: self.drive_start_date,
        drive_end_date: self.drive_end_date,
        user_name: self.user_name,
        user_sex: self.user_sex,
        user_age: self.user_age,
        user_ident: self.user_ident,
        user_tel: self.user_tel,
        user_office: self.user_office,
        user_addr: self.user_addr,
        user_post: self.user_post,
        user_email: self.user_email
      }).then(function (response) {
        self.$message('修改成功')
      }).catch(e => {
        self.$message('修改失败')
        this.errors.push(e)
      })
    }
  }
}
</script>
<style scoped>
.input{
  min-width: 193px;
}
.row{
  margin-top: 50px;
}
h3{
  margin-left: 100px;
}
</style>
