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
            <el-button type="primary" @click="submitForm('form')">提交</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    export default {
      data () {
        return {
          form: {
            account: '',
            password: ''
          }
        }
      }
    }
</script>

<style scoped>

</style>
