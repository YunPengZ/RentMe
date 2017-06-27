<template>
<div>
<!--<el-row class="singlerow">
  <el-col>
    <el-button class="button" type="primary">
      提交
    </el-button>
  </el-col>
</el-row>-->
<el-row justify="center">
<el-form :inline="true"  class="demo-form-inline">
  <el-form-item label="车辆号码">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>

    <el-form-item label="车辆型号">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
    <el-form-item label="车辆颜色">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
    <el-form-item label="发动机号">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
   </el-form-item>
    <el-form-item label="车架编号">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>

</el-form>
<el-form :inline="true"  class="demo-form-inline">
  <el-form-item label="购买日期">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
    <el-form-item label="销售商">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
    <el-form-item label="状态">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
    <el-form-item label="保单号">
    <el-input v-model="formInline.user" placeholder="审批人"></el-input>
  </el-form-item>
  </el-row>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">查询</el-button>
  </el-form-item>
</el-form>
<el-row type="flex" justify="center">
<el-col>
  <el-table
    :data="users"
    border
    highlight-current-row
    @current-change="handleCurrentChange"
    style="width: 100%"
    :default-sort = "{prop: 'date', order: 'descending'}"
    >
    <el-table-column
      prop="match_ID"
      label="比赛编号"
      sortable
      >
    </el-table-column>
    <el-table-column
      prop="user_ID"
      label="选手编号">
    </el-table-column>
    <el-table-column
      prop="match_Grade"
      label="成绩"
      width="180"
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
      users: [
        {
          match_ID: 'fuckyou',
          user_ID: '234',
          match_Grade: null
        }
      ],
      currentRow: {
        match_ID: '123',
        user_ID: '234',
        match_Grade: null
      },
      formInline: {
        user: 'fucker',
        region: 'you'
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
  .singlerow {
    margin-top: 40px;
  }
  .button {
    width: 100%;
  }
</style>
