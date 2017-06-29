<template>
  <div>
 
      <el-row>
          
              
        <el-col :offset="4" :span="16">
            <el-card class="cardPosition">
                  <h3>添加门店管理员信息</h3>
          <el-form :model="ruleForm" label-width="100px">
            <el-form-item >
            <el-input placeholder="请输入内容" v-model="formInline.admin_name" >
                <template slot="prepend">姓名</template>
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.admin_sex" >
                <template slot="prepend">性别</template>
            </el-input>
            </el-form-item>
            <el-form-item >
            <el-input placeholder="请输入内容" v-model="formInline.admin_age" >
                <template slot="prepend">年龄</template>
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.admin_ident" >
                <template slot="prepend">身份证</template>
            </el-input>
            </el-form-item>
                        <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.admin_tel" >
                <template slot="prepend">电话</template>
            </el-input>
            </el-form-item>
                        <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.admin_email" >
                <template slot="prepend">EMAIL</template>
            </el-input>
            </el-form-item>
                        <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.admin_type" >
                <template slot="prepend">管理员类型</template>
            </el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="addManager">提交</el-button>
            </el-form-item>
          </el-form>
          </el-card>
              </el-col>
          
      </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      formInline: {
        admin_id: '',
        admin_name: '',
        admin_sex: '',
        admin_age: '',
        admin_ident: '',
        admin_tel: '',
        admin_email: '',
        admin_type: ''
      }
    }
  },
  methods: {
    addManager () {
      var self = this
      axios.post('/test/admins/', {
        statu: 'add',
        admin_name: self.formInline.admin_name,
        admin_sex: self.formInline.admin_sex,
        admin_age: self.formInline.admin_age,
        admin_ident: self.formInline.admin_ident,
        admin_tel: self.formInline.admin_tel,
        admin_email: self.formInline.admin_email,
        admin_type: self.formInline.admin_type
      })
            .then(function (response) {
              self.$message('添加成功')
            })
            .catch(e => {
              self.$message('添加失败')
              this.errors.push(e)
            })
    }
  }
}
</script>
<style scoped>
.text{
  font-size: 5px;
  color:grey;
}
h3{
  margin-left: 100px;
}
.cardPosition{
    margin-top: 40px;
}
</style>
