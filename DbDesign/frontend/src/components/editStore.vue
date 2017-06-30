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
                <el-button type="primary" @click="updateStore">提交</el-button>
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
        store_id: '',
        store_addr: '',
        store_tel: '',
        store_start_time: '',
        store_admin: ''
      }
    }
  },
  created () {
    var self = this
    var id = [self.$route.params.id]
    // console.log(id)
    axios.post('/test/stores/', {
      'statu': 'query',
      store_id: id
    })
         .then(function (response) {
           self.formInline = response.data[0]
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    updateStore () {
      var self = this
      var id = [self.$route.params.id]
      axios.post('/test/stores/', {
        'statu': 'update',
        store_id: id,
        store_addr: self.formInline.store_addr,
        store_tel: self.formInline.store_tel,
        store_start_time: self.formInline.store_start_time,
        store_admin: self.formInline.store_admin
      })
            .then(function (response) {
              self.$message('修改成功')
            })
            .catch(e => {
              self.$message('修改失败')
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
