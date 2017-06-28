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
                <el-button type="primary">提交</el-button>
            </el-form-item>
          </el-form>
          </el-card>
              </el-col>
          
      </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      formInline: {
        admin_name: '12987132',
        admin_sex: '123',
        admin_age: '红色',
        admin_ident: '45432',
        admin_tel: '18756010918',
        admin_email: '2087447114@qq.com',
        admin_type: '大中华区管理员'
      }
    }
  },
  methods: {
    handleCheckAllChange (event) {
    },
    handleCheckedCitiesChange (value) {
      let checkedCount = value.length
      this.checkAll = checkedCount === this.options['car_type'].length
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.options['car_type'].length
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
