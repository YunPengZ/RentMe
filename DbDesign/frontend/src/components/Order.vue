<template>
  <div>
    <el-row type="flex"  class="row">
      <el-col :span="12" :offset="4">
        <el-input
          placeholder="搜索订单"
          icon="search"
          v-model="input"
          :on-icon-click="handleIconClick">
        </el-input>
      </el-col>
      <el-col :span="2" :offset="2">
        <router-link to="/home/new_order" class="text">
          <el-button type="primary">
            <i class="el-icon-plus"> 添加订单</i> 
          </el-button>
        </router-link>
      </el-col>
    </el-row>
    <el-row type="flex" justify="space-between"  class="row">
      <el-col :span="16" :offset="4">
          <el-table
            ref="multipleTable"
            :data="tableData3"
            tooltip-effect="dark"
            @selection-change="handleSelectionChange">
            <el-table-column
              type="index"
              width="50">
            </el-table-column>
            <el-table-column type="expand">
              <template scope="props">
              <el-form label-position="left" inline>
                <el-row v-for="(relet_record, index) in props.row.relet_records" :key="relet_record.relet_id">
                  <el-form-item>第{{ index + 1 }}次续租:</el-form-item>
                  <el-form-item  label="续租起始时间">{{ relet_record.relet_start_time }}</el-form-item>
                  <el-form-item  label="续租结束时间">{{ relet_record.relet_end_time }}</el-form-item>
                </el-row>
              </el-form>
              </template>
            </el-table-column>
            <el-table-column
              prop="car_num"
              label="车牌号">
            </el-table-column>
            <el-table-column
              prop="user_name"
              label="用户名称">
            </el-table-column>
            <el-table-column
              prop="drive_name"
              label="驾驶人名称">
            </el-table-column>
            <el-table-column
              prop="pick_addr"
              label="取车门店号">
            </el-table-column>
            <el-table-column
              prop="pick_time"
              label="取车时间">
            </el-table-column>
            <el-table-column
              prop="drop_time"
              label="还车时间">
            </el-table-column>
            <el-table-column
              label="操作"
              width="100">
              <template scope="props">
                <el-button type="text" size="small" @click="relet(props.row)">续租</el-button>
                <el-button type="text" size="small" @click="charge(props.row)">回收</el-button>
              </template>
            </el-table-column>
          </el-table>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      input: '',
      tableData3: []
    }
  },
  created () {
    var self = this
    axios.get('/test/order', {}).then(function (response) {
      self.tableData3 = response.data
    }).catch(e => {
      this.errors.push(e)
    })
  },
  methods: {
    charge (order) {
      const h = this.$createElement
      this.$msgbox({
        title: '费用收取',
        message: h('div', null, [
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '违章费用: ' + order.illegal_bill)
          ]),
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '维修费用: ' + order.breaken_bill)
          ]),
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '时间费用: ' + (0 - order.actual_deposit))
          ]),
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '押金退还: ' + (0 - order.actual_deposit))
          ]),
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '最终款: ' + (order.illegal_bill + order.breaken_bill - order.actual_deposit))
          ])
        ]),
        showCancelButton: true,
        confirmButtonText: '确认回收',
        cancelButtonText: '取消',
        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            instance.confirmButtonLoading = true
            instance.confirmButtonText = '执行中...'
            setTimeout(() => {
              done()
              setTimeout(() => {
                instance.confirmButtonLoading = false
              }, 300)
            }, 3000)
          } else {
            done()
          }
        }
      }).then(action => {
        this.$message({
          type: 'info',
          message: '订单回收: ' + action
        })
      })
    },
    relet (order) {
      const h = this.$createElement
      this.$msgbox({
        title: '费用收取',
        message: h('div', null, [
          h('el-row', {style: 'margin-top: 20px'}, [
            h('el-col', null, '续租费用: ' + order.car_day_price)
          ])
        ]),
        showCancelButton: true,
        confirmButtonText: '确认续租',
        cancelButtonText: '取消',
        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            instance.confirmButtonLoading = true
            instance.confirmButtonText = '执行中...'
            setTimeout(() => {
              done()
              setTimeout(() => {
                instance.confirmButtonLoading = false
              }, 300)
            }, 3000)
          } else {
            done()
          }
        }
      }).then(action => {
        this.$message({
          type: 'info',
          message: '续租: ' + action
        })
      })
    },
    handleIconClick (event) {
      console.log(event)
    }
  }
}
</script>
<style scoped>
  .text{
    color: aliceblue;
    text-decoration: none;
  }
  .row{
    margin-top: 50px;
  }
</style>
