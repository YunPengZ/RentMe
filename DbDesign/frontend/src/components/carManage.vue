<template>
<div>
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
  placeholder="请输入内容"
  @select="handleSelect"
  icon="edit"
  :on-icon-click="handleIconClick"
>
</el-autocomplete>
</el-row>
<el-row type="flex">
<el-col :offset="4" :span="16">
  <el-table
    :data="table"
    border
    highlight-current-row
    @current-change="handleCurrentChange"
    style="width: 100%"
    :default-sort = "{prop: 'date', order: 'descending'}"
    >
    <el-table-column
      prop="millegal_car_num"
      label="车牌号码"
      width="120"
      sortable
      >
    </el-table-column>
    <el-table-column
      prop="illegal_date"
      label="违章时间"
      width="100"
      >
      
    </el-table-column>
    <el-table-column
      prop="illegal_bill"
      label="违章金额"
      width="100"
    >
    </el-table-column>
        <el-table-column
      prop="illegal_info"
      label="违章信息"
      
    >
    </el-table-column>
  </el-table>
</el-col>
</el-row>
</div>
</template>
<script>
// import axios from 'axios';
export default {
  data () {
    return {
      table: [
        {
          millegal_car_num: 'fuckyou',
          illegal_date: '234',
          illegal_bill: '1001000$',
          illegal_info: 'xyz'
        },
        {
          millegal_car_num: 'fuckyou-1',
          illegal_date: '234',
          illegal_bill: '1001000$',
          illegal_info: 'xyz'
        }
      ],
      currentRow: {
        match_ID: '123',
        user_ID: '234',
        match_Grade: null
      },
      formInline: {
        millegal_car_num: 'fuckyou',
        illegal_date: '',
        illegal_bill: '1001000$',
        illegal_info: 'xyz'
      },
      displayStatus: false
    }
  }
//     created() {
//     var self = this;
//     var id = self.$route.params.id;
//     axios.get('/api/user/queryAllGrade',{
//       params: {
//       message : id
//     }
//     })
//       .then( function (response) {
//        self.users = response.data
//       })
//       .catch(e => {
//       this.errors.push(e)
//     })
//   },
//   methods: {
//     handleCurrentChange (val) {
//       this.currentRow = val
//       this.displayStatus = true
//     },
//     submit(){
//             var self = this;
//             var grade = self.currentRow.match_Grade;
//             var m_id = self.currentRow.match_ID;
//             var u_id = self.currentRow.user_ID;
//             axios.post('/api/user/inputGrade',{
//             match_Grade: grade,
//             match_ID: m_id,
//             user_ID: u_id
//             })
//             .then(function (response) {
//             self.$message('成绩提交成功')
//             })
//             .catch(e => {
//               this.errors.push(e)
//             })
//     }
//   }
}
</script>
<style scoped>
  .firstRow {
    margin-top: 40px;
    justify-content: center; 
  }
  .button {
    width: 100%;
  }
</style>
