<template>
  <div>
    <el-card>
      <el-row>
        <h3>预订车辆</h3>
        <el-col :span="8">
          <img src="../assets/car.jpg" class="image">
        </el-col>
        <el-col :span="16">
          <el-row>
            <el-col :span="12">
              <p>车牌号：{{car_num}}</p>
            </el-col>
            <el-col :span="12">
              <p>品牌：{{car_brand}}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <p>车系：{{car_series}}</p>
            </el-col>
            <el-col :span="12">
              <p>配置：{{car_config_model}}</p>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-card>
    <el-row class="row">
      <el-col :span="11">
        <el-card>
          <el-row>
            <el-col :span="12">
              <p>用户姓名：{{this.user_name}}</p>
            </el-col>
            <el-col :span="12">
              <p>驾驶员姓名：{{this.drive_name}}</p>
            </el-col>
          </el-row>
          <el-row class="row">
            <el-col :span="24">
              <el-input v-model="form.pick_addr" auto-complete="off">
                <template slot="prepend">取车门店</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row  class="row">
            <el-col :span="12">
              <el-date-picker
                v-model="form.pick_time"
                type="date"
                placeholder="取车时间">
              </el-date-picker>
            </el-col>
            <el-col :span="12">
              <el-date-picker
                v-model="form.drop_time"
                type="date"
                placeholder="还车时间">
              </el-date-picker>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="11" :offset="2">
        <el-card>
          <el-row>
            <p>车型押金：{{car_deposit}}</p>
          </el-row>
          <el-row>
            <p>时间押金：{{time_deposit}}</p>
          </el-row>
          <el-row>
            <el-col :span="10">
              <p>信用押金：</p>
            </el-col>
            <el-col :span="14">
              <el-input v-model="input"></el-input>
            </el-col>
          </el-row>
          <el-row>
            <p>实收押金：{{actual_deposit}}</p>
          </el-row>
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
      form: {
        pick_addr: null,
        pick_time: null,
        drop_time: null
      },
      user_deposit: null,
      car_deposit: 5000,
      car_model_id: null,
      car_day_price: 100,
      user_name: '小明',
      drive_name: '小红',
      car_num: '皖A23124',
      car_brand: '宝马',
      car_series: '汉兰达',
      car_config_model: '豪华型'
    }
  },
  created () {
    axios.get('/test/user/' + this.$store.state.order_user_id, {})
    .then(function (response) {
      this.user_name = response.data.user_name
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/licenses/' + this.$store.state.order_drive_id, {})
    .then(function (response) {
      this.drive_name = response.data.drive_name
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/car/' + this.$store.state.car_ID, {})
    .then(function (response) {
      this.car_num = response.data.car_num
      this.car_model_id = response.data.car_model_id
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/model/' + this.$store.state.car_model_id, {})
    .then(function (response) {
      this.car_deposit = response.data.car_deposit
      this.car_day_price = response.data.car_day_price
      this.car_brand = response.data.car_brand
      this.car_series = response.data.car_series
      this.car_config_model = response.data.car_config_model
    }).catch(e => {
      this.errors.push(e)
    })
  },
  computed: {
    time_deposit () {
      if (this.form.drop_time === undefined || this.form.pick_time === undefined) {
        return 0
      } else {
        return (this.form.drop_time - this.form.pick_time) / 86400000 * this.car_day_price
      }
    },
    actual_deposit () {
      if (this.user_deposit === null || this.user_deposit === undefined) {
        return this.time_deposit + this.car_deposit
      } else {
        return this.user_deposit + this.time_deposit + this.car_deposit
      }
    }
  }
}
</script>
<style scoped>
.row {
  margin-top: 50px;
}
h3 {
  margin: 0px 0px 10px 0px;
}
.image {
  height: 150px;
  width: 150px;
  display: block;
}
</style>
