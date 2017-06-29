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
        rows: [
          { 'pick_time': '2017-01-01', 'store_count1': 10, 'store_count2': 26, 'store_count3': 1, 'store_count4': 2, 'store_count5': 12 },
          { 'pick_time': '2017-01-02', 'store_count1': 23, 'store_count2': 27, 'store_count3': 31, 'store_count4': 32, 'store_count5': 33 },
          { 'pick_time': '2017-01-03', 'store_count1': 13, 'store_count2': 12, 'store_count3': 21, 'store_count4': 12, 'store_count5': 33 },
          { 'pick_time': '2017-01-04', 'store_count1': 50, 'store_count2': 32, 'store_count3': 8, 'store_count4': 2, 'store_count5': 23 },
          { 'pick_time': '2017-01-05', 'store_count1': 33, 'store_count2': 16, 'store_count3': 13, 'store_count4': 32, 'store_count5': 13 },
          { 'pick_time': '2017-01-06', 'store_count1': 1, 'store_count2': 23, 'store_count3': 11, 'store_count4': 12, 'store_count5': 50 },
          { 'pick_time': '2017-01-07', 'store_count1': 12, 'store_count2': 21, 'store_count3': 21, 'store_count4': 32, 'store_count5': 13 },
          { 'pick_time': '2017-01-08', 'store_count1': 6, 'store_count2': 4, 'store_count3': 1, 'store_count4': 2, 'store_count5': 3 }
        ]
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
    axios.get('/test/order/type/?format=json', {})
    .then(function (response) {
      this.typeData.rows = response.data
      console.log(response.data)
    }).catch(e => {
      this.errors.push(e)
    })
    axios.get('/test/order/date/?format=json', {})
    .then(function (response) {
      this.dayData.rows = response.data
      console.log(response.data)
    }).catch(e => {
      this.errors.push(e)
    })
    // axios.get('/test/order/date_type/?format=json', {})
    // .then(function (response) {
    //   for (var LenCount = 0; LenCount < response.data.length; LenCount++) {
    //     var justifyData = response.data[LenCount]['store_count']
    //     this.dayData.rows.push(response.data[LenCount])
    //   }
    //   this.dayData.rows = response.data
    // }).catch(e => {
    //   this.errors.push(e)
    // })
  }
}
</script>
<style scoped>
</style>
