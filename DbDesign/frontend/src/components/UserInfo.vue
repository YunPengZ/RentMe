<template>
  <div>
    <el-row>
      <el-card>
        <el-col :span="12">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item prop="name">
            <el-input v-model="ruleForm.name" auto-complete="off">
              <template slot="prepend">姓名</template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <template>
              <el-radio class="radio" v-model="ruleForm.sex" label="男">男</el-radio>
              <el-radio class="radio" v-model="ruleForm.sex" label="女">女</el-radio>
            </template>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="ruleForm.aage">
              <template slot="prepend">年龄</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="ruleForm.aage">
              <template slot="prepend">电话</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="ruleForm.aage">
              <template slot="prepend">身份证号</template>
            </el-input>
          </el-form-item>
        </el-form>
        </el-col>
        <el-col :span="12">
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item prop="pass">
            <el-input type="password" v-model="ruleForm.password" auto-complete="off">
              <template slot="prepend">地址</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="checkPass">
            <el-input type="password" v-model="ruleForm.password" auto-complete="off">
              <template slot="prepend">邮编</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="ruleForm.aage">
              <template slot="prepend">Email</template>
            </el-input>
          </el-form-item>
          <el-form-item prop="age">
            <el-input v-model.number="ruleForm.aage">
              <template slot="prepend">工作单位</template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          </el-form-item>
        </el-form>
        </el-col>
      </el-card>
    </el-row>
    <el-row>
    </el-row>
  </div> 
</template>
<script>
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
      ruleForm: {
        sex: '',
        pass: '',
        checkPass: '',
        age: ''
      },
      rules: {
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>
<style scoped>
el-form-item{
  margin-left: 0px;
}
</style>
