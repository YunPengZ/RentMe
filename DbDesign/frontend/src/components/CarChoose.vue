<template>
<div >
<!--<el-row class="singlerow">
  <el-col>
    <el-button class="button" type="primary">
      提交
    </el-button>
  </el-col>
</el-row>-->
<el-row type="flex" class="firstRow">
<el-autocomplete
  popper-class="my-autocomplete"
  v-model="state3"
  :fetch-suggestions="querySearch"
  custom-item="my-item-zh"
  placeholder="搜索车辆"
  @select="handleSelect"
  icon="edit"
  :on-icon-click="handleIconClick"
>
</el-autocomplete>
<router-link :to="'/home/addCar'"  class="rid" v-if="$route.path !== '/home/new_order/car_choose'">
<el-button type="primary" icon="edit" class="addButton">添加车辆信息</el-button>
</router-link>
</el-row>
<el-row type="flex" class="secondRow">
<el-col :offset="4" :span="17">
  <el-table
    :data="table"
    height="600"
    style="width: 100%">
    
        <el-table-column
      type="index"
      >
    </el-table-column>
    <el-table-column type="expand">
      <template scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="购买日期">
            <span>{{ props.row.car_buy_date }}</span>
          </el-form-item>
          <el-form-item label="销售商">
            <span>{{ props.row.car_retailer }}</span>
          </el-form-item>
          <el-form-item label="状态">
            <span>{{ props.row.car_status }}</span>
          </el-form-item>
          <el-form-item label="保单号">
            <span>{{ props.row.car_ins_num }}</span>
          </el-form-item>
          <el-form-item label="创建者">
            <span>{{ props.row.car_creater }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>

    <el-table-column
      label="车辆号码"
      prop="car_num">
    </el-table-column>
    <el-table-column
      label="车辆型号"
      prop="car_model_id">
    </el-table-column>
    <el-table-column
      label="车辆颜色"
      prop="car_color">
    </el-table-column>
    <el-table-column
      label="发动机号"
      prop="car_engine_num">
    </el-table-column>
        <el-table-column
      label="车架编号"
      prop="car_frame_num">
    </el-table-column>
    <el-table-column
      label="操作"
      >
      <template scope="props">
        <el-button size="small" type="primary" @click="chooseCar(props.row)">选中</el-button>
      </template>
    </el-table-column>
  </el-table>
</el-col>
</el-row>
</div>
</template>
<script>
// import axios from 'axios'
export default {
  data () {
    return {
      table: [
      // {
      //   car_num: '12987132',
      //   car_model_id: '123',
      //   car_color: '红色',
      //   car_engine_num: '45432',
      //   car_frame_num: '47186',
      //   car_buy_date: '2016-2-3',
      //   car_retailer: '10333',
      //   car_status: '已租',
      //   car_ins_num: '123456',
      //   car_creater: 'kinmin'
      // }
      ]
    }
  },
  created () {
    var self = this
    self.table = self.$store.state.matched_car
  },
  methods: {
    chooseCar (event) {
      var self = this
      console.log('click')
      self.$store.state.car_ID = event.car_id
      self.$store.state.car_model_id = event.car_model_id_id
      self.$store.state.step = 3
      self.$message('车辆选择成功')
      self.$router.push('/home/new_order/order_charge')
      self.$router.go(1)
    }
  }
}
</script>
<style scoped>
  .firstRow {
    margin-top: 40px;

    justify-content: center; 
  }
  .secondRow {
      margin-top: 40px; 
  }
  .button {
    width: 100%;
  }
  .addButton {
    margin-left:300px; 
  }
</style>
