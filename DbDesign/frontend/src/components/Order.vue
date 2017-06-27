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
              type="selection"
              width="50">
            </el-table-column>
            <el-table-column type="expand">
              <template scope="props">
              <el-form label-position="left" inline>
                <el-row v-for="(relet_record, index) in props.row.relet_records" :key="relet_record.relet_id">
                  <el-form-item  label="续租号">{{ index + 1 }}</el-form-item>
                  <el-form-item  label="续租起始时间">{{ relet_record.relet_start_time }}</el-form-item>
                  <el-form-item  label="续租结束时间">{{ relet_record.relet_end_time }}</el-form-item>
                </el-row>
              </el-form>
              </template>
            </el-table-column>
            <el-table-column
              prop="date"
              label="订单时间">
              <template scope="scope">{{ scope.row.date }}</template>
            </el-table-column>
            <el-table-column
              prop="name"
              label="订单编号">
            </el-table-column>
            <el-table-column
              prop="name"
              label="用户名">
            </el-table-column>
            <el-table-column
              prop="address"
              label="车牌号">
            </el-table-column>
            <el-table-column
              prop="name"
              label="门店号">
            </el-table-column>
            <el-table-column
              prop="name"
              label="取车时间">
            </el-table-column>
            <el-table-column
              label="操作"
              width="100">
              <template scope="scope">
                <el-button type="text" size="small">修改</el-button>
                <el-button type="text" size="small">回收</el-button>
              </template>
            </el-table-column>
          </el-table>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      input: '',
      tableData3: [{
        date: '2016-05-03',
        name: '王小虎',
        address: ' 1518 弄',
        relet_records: [
          {relet_id: 1, relet_start_time: '2016-05-03', relet_end_time: '2016-05-04'},
          {relet_id: 2, relet_start_time: '2016-05-04', relet_end_time: '2016-05-05'}
        ]
      }, {
        date: '2016-05-02',
        name: '王小虎',
        address: ' 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: ' 1518 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: ' 1518 弄'
      }],
      multipleSelection: []
    }
  },
  methods: {
    handleIconClick (event) {
      console.log(event)
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
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
