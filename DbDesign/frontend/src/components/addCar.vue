<template>
  <div>
      <el-row type="flex" justify="center">
          <h1>添加车辆信息</h1>
          </el-row>
      <el-row type="flex" justify="center">
          <el-form :model="ruleForm" label-width="100px">
            <el-form-item label="车辆号码">
            <el-input placeholder="请输入内容" v-model="formInline.car_num" >
            </el-input>
            </el-form-item>
            <el-form-item label="车辆型号">
            <el-input placeholder="请输入内容" v-model="formInline.car_model_id" >
            </el-input>
            </el-form-item>
            <el-form-item label="车辆颜色">
            <el-input placeholder="请输入内容" v-model="formInline.car_color" >

            </el-input>
            </el-form-item>
            <el-form-item label="发动机号">
            <el-input placeholder="请输入内容" v-model="formInline.car_engine_num" >

            </el-input>
            </el-form-item>
            <el-form-item label="车架编号">
            <el-input placeholder="请输入内容" v-model="formInline.car_frame_num" >

            </el-input>
            </el-form-item>
            <el-form-item label="购买日期">
                    <el-date-picker
      v-model="formInline.car_buy_date"
      type="date"
      :picker-options="pickerOptions0">
    </el-date-picker>

            </el-input>
            </el-form-item>
            <el-form-item label="销售商">
            <el-input placeholder="请输入内容" v-model="formInline.car_retailer" >

            </el-input>
            </el-form-item>
            <el-form-item label="状态">
            <el-input placeholder="请输入内容" v-model="formInline.car_status" >

            </el-input>
            </el-form-item>
            <el-form-item label="保单号">
            <el-input placeholder="请输入内容" v-model="formInline.car_ins_num" >
               
            </el-input>
            </el-form-item>
          </el-form>
       
      </el-row>
      <el-row type="flex" justify="center">
        
          <el-button type="primary">提交</el-button>
     
      </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      formInline: {
        car_num: '',
        car_model_id: '',
        car_color: '',
        car_engine_num: '',
        car_frame_num: '',
        car_buy_date: '',
        car_retailer: '',
        car_status: '',
        car_ins_num: '',
        car_creater: ''
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
</style>
