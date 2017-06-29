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
        
          <el-button type="primary" @click="updateCar(this.$route.params.id)">提交</el-button>
     
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
        updateCar (car_num) {
          var self = this
          console.log(self.form.account)
          axios.post('/test/login/?format=json', {
            admin_tel: self.form.account,
            admin_pas: self.form.password
          })
            .then(function (response) {
              self.$message('登录成功')
              self.$store.state.user_Name = response.data['admin_name']
              self.$store.state.user_ID = response.data['user_ID']
              self.$store.state.user_Status = response.data['user_Status']
              self.$router.push('/home')
              self.$router.go(1)
            })
            .catch(e => {
              self.$message('账号或者密码错误，请重新输入')
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
