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
              <el-select v-model="form.pick_addr" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
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
            <p>实收押金：{{actual_deposit}}</p>
          </el-row>
          <el-row class="min-row">
            <el-button type="primary" @click="handleSubmit()">提交订单</el-button>
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
      options: [{
        value: 1,
        label: '一号门店'
      }, {
        value: 2,
        label: '二号门店'
      }, {
        value: 3,
        label: '三号门店'
      }, {
        value: 4,
        label: '四号门店'
      }, {
        value: 5,
        label: '五号门店'
      }],
      form: {
        pick_addr: null,
        pick_time: null,
        drop_time: null
      },
      user_deposit: null,
      car_deposit: null,
      car_model_id: null,
      car_day_price: null,
      user_name: null,
      drive_name: null,
      car_num: null,
      car_brand: null,
      car_series: null,
      car_config_model: null
    }
  },
  created () {
    var self = this
    axios.get('/test/user/' + this.$store.state.order_user_id, {})
    .then(function (response) {
      self.user_name = response.data.user_name
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/licenses/' + this.$store.state.order_drive_id, {})
    .then(function (response) {
      self.drive_name = response.data.drive_name
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/car/' + this.$store.state.car_ID, {})
    .then(function (response) {
      self.car_num = response.data.car_num
      self.car_model_id = response.data.car_model_id
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/model/' + this.$store.state.car_model_id, {})
    .then(function (response) {
      self.car_deposit = response.data.car_deposit
      self.car_day_price = response.data.car_day_price
      self.car_brand = response.data.car_brand
      self.car_series = response.data.car_series
      self.car_config_model = response.data.car_config_model
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
  },
  methods: {
    handleSubmit () {
      var self = this
      axios.post('/test/order/pay', {
        user_num: self.$store.state.order_user_id,
        car_num: self.$store.state.car_ID,
        relet_order: [],
        actual_deposit: self.actual_deposit,
        pick_addr: self.form.pick_addr,
        pick_time: self.form.pick_time,
        drop_time: self.form.drop_time,
        user_drive: self.$store.state.order_drive_id,
        record_create_admin: self.$store.state.user_ID
      }).then(function (response) {
        self.$message('订单成功')
      }).catch(e => {
        self.$message('订单失败')
        this.errors.push(e)
      })
    }
  }
}
</script>
<style scoped>
.row {
  margin-top: 50px;
}
.min-row {
  margin-top: 15px;
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
