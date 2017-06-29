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
        
          <el-button type="primary" @click="addCar">提交</el-button>
     
      </el-row>
  </div>
</template>
<script>
import axios from 'axios'
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
    addCar () {
      var self = this
      console.log(self.form.account)
      axios.post('/test/car/', {
        status: 'add',
        car_num: self.formInline.car_num,
        car_model_id: self.formInline.car_model_id,
        car_color: self.formInline.car_color,
        car_engine_num: self.formInline.car_engine_num,
        car_frame_num: self.formInline.car_frame_num,
        car_buy_date: self.formInline.car_buy_date,
        car_retailer: self.formInline.car_retailer,
        car_status: self.formInline.car_status,
        car_ins_num: self.formInline.car_ins_num,
        car_creater: self.$store.state.user_ID
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
</style>
