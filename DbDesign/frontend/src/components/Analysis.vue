<template>
  <div>
    <el-row>
      <el-col :span="9" :offset="2">
        <h3>各车型出租情况</h3>
        <ve-pie :data="typeData" :settings="typeSettings" tooltip-visible legend-visible></ve-pie>
      </el-col>
      <el-col :span="9" :offset="2">
        <h3>日出租情况</h3>
        <ve-line :data="dayData" :settings="daySettings" tooltip-visible legend-visible></ve-line>
      </el-col>
    </el-row>
    <el-row>
      <el-col :offset="7" :span="10">
        <h3>门店出租情况</h3>
        <ve-histogram :data="storeData" :settings="storeSettings" tooltip-visible legend-visible></ve-histogram>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      typeData: {
        columns: ['车型', '租出数'],
        rows: [{pick_time: '商务车', car_count: 11},
        {pick_time: 'SUV', car_count: 30},
        {car_type: 'ETC', car_count: 20}]
      },
      typeSettings: {
        dimension: 'car_type',
        metrics: 'car_count',
        dataType: 'KMB',
        selectedMode: 'single',
        hoverAnimation: true,
        radius: 100,
        offsetY: 200
      },
      dayData: {
        columns: ['日期', '租出数'],
        rows: [{pick_time: '2017-06-01', car_count: 12},
        {pick_time: '2017-06-02', car_count: 22},
        {pick_time: '2017-06-03', car_count: 16},
        {pick_time: '2017-06-04', car_count: 32},
        {pick_time: '2017-06-05', car_count: 27}]
      },
      daySettings: {
        dimension: ['pick_time'],
        metrics: ['car_count'],
        yAxisType: ['KMB'],
        yAxisName: ['租出数'],
        area: true
      },
      storeData: {
        columns: ['日期', '门店1', '门店2', '门店3', '门店4', '门店5'],
        rows: [{pick_time: '2017-06-01', store_count1: 12, store_count2: 21, store_count3: 40, store_count4: 16, store_count5: 25},
        {pick_time: '2017-06-02', store_count1: 22, store_count2: 11, store_count3: 20, store_count4: 18, store_count5: 33},
        {pick_time: '2017-06-03', store_count1: 12, store_count2: 31, store_count3: 31, store_count4: 12, store_count5: 22},
        {pick_time: '2017-06-04', store_count1: 32, store_count2: 11, store_count3: 5, store_count4: 14, store_count5: 12},
        {pick_time: '2017-06-05', store_count1: 28, store_count2: 31, store_count3: 24, store_count4: 17, store_count5: 32}]
      },
      storeSettings: {
        dimension: ['pick_time'],
        metrics: ['store_count1', 'store_count2', 'store_count3', 'store_count4', 'store_count5'],
        yAxisType: ['KMB'],
        yAxisName: ['出租数'],
        stack: {
          '总出租数': ['store_count1', 'store_count2', 'store_count3', 'store_count4', 'store_count5']
        }
      }
    }
  },
  created () {
    var self = this
    axios.get('/test/order/type', {})
    .then(function (response) {
      self.typeData.rows = response.data
    }).catch(e => {
      this.errors.push(e)
    })
    // axios.get('/test/order/date', {})
    // .then(function (response) {
    //   self.dayData.rows = response.data
    // }).catch(e => {
    //   this.errors.push(e)
    // })
    // axios.get('/test/order/date_type', {})
    // .then(function (response) {
    //   self.storeData.rows = response.data
    // }).catch(e => {
    //   this.errors.push(e)
    // })
  }
}
</script>
<style scoped>
</style>
