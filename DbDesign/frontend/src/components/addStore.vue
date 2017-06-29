<template>
  <div>
 
      <el-row>
          
              
        <el-col :offset="4" :span="16">
            <el-card class="cardPosition">
                  <h3>添加门店信息</h3>
          <el-form :model="ruleForm" label-width="100px">
            <el-form-item >
            <el-input placeholder="请输入内容" v-model="formInline.store_addr" >
                <template slot="prepend">门店地址</template>
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.store_tel" >
                <template slot="prepend">门店联系方式</template>
            </el-input>
            </el-form-item>
            <el-form-item >
            <el-input placeholder="请输入内容" v-model="formInline.store_start_time" >
                <template slot="prepend">门店营业时间</template>
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-input placeholder="请输入内容" v-model="formInline.store_admin" >
                <template slot="prepend">门店管理员</template>
            </el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="addStore">提交</el-button>
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
        store_addr: '',
        store_tel: '',
        store_start_time: '',
        store_admin: ''
      }
    }
  },
  methods: {
    addStore () {
      var self = this
      console.log(self.form.account)
      axios.post('/test/stores/', {
        store_addr: self.formInline.store_addr,
        store_tel: self.formInline.store_tel,
        store_start_time: self.formInline.store_start_time,
        store_admin: self.formInline.store_admin
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
