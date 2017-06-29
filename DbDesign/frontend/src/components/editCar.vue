<template>
  <div>
      <el-row type="flex" justify="center">
          <h1>修改车辆信息</h1>
          </el-row>
      <el-row type="flex" justify="center">
          <el-form :model="formInline" label-width="100px">
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
        
          <el-button type="primary" @click="updateCar">提交</el-button>
     
      </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      formInline: {
        // car_num: '12987132',
        // car_model_id: '123',
        // car_color: '红色',
        // car_engine_num: '45432',
        // car_frame_num: '47186',
        // car_buy_date: '2016-2-3',
        // car_retailer: '10333',
        // car_status: '已租',
        // car_ins_num: '123456',
        // car_creater: 'kinmin'
      }
    }
  },
  created () {
    var self = this
    var id = self.$route.params.id
    axios.get('/test/car/?format=json', {
      params: {
        car_num: id
      }
    })
         .then(function (response) {
           self.formInline = response.data[0]
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    updateCar () {
      var self = this
      console.log(self.form.account)
      axios.post('/test/car', {
        car_id: self.formInline.car_id,
        car_num: self.formInline.car_num,
        car_model_id: self.formInline.car_model_id,
        car_color: self.formInline.car_color,
        car_engine_num: self.formInline.car_engine_num,
        car_frame_num: self.formInline.car_frame_num,
        car_buy_date: self.formInline.car_buy_date,
        car_retailer: self.formInline.car_retailer,
        car_status: self.formInline.car_status,
        car_ins_num: self.formInline.car_ins_num,
        car_creater: self.formInline.car_creater
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
</style>
