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
        store_addr: '12987132',
        store_tel: '123',
        store_start_time: '红色',
        store_admin: '45432'
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
