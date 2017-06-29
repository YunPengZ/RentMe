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
        rows: []
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
        rows: []
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
        rows: []
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
    axios.get('/test/order/date', {})
    .then(function (response) {
      self.dayData.rows = response.data
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/order/date_type', {})
    .then(function (response) {
      self.storeData.rows = response.data
    }).catch(e => {
      this.errors.push(e)
    })
  }
}
</script>
<style scoped>
</style>
