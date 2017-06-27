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
  placeholder="搜索车辆"
  @select="handleSelect"
  icon="edit"
  :on-icon-click="handleIconClick"
>
</el-autocomplete>

<el-button type="primary" icon="edit" class="addButton">添加车辆信息</el-button>
</el-row>
<el-row type="flex" class="secondRow">
<el-col :offset="4" :span="16">
  <el-table
    :data="table"
    style="width: 100%">
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
      prop="desc">
            <template scope="scope">
                <router-link :to="'/home/editCar'"  class="rid">
        <el-button
          size="small">            
          
              编辑
            
            </el-button>
            </router-link>

        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
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
      table: [{
        car_num: '12987132',
        car_model_id: '123',
        car_color: '红色',
        car_engine_num: '45432',
        car_frame_num: '47186',
        car_buy_date: '2016-2-3',
        car_retailer: '10333',
        car_status: '已租',
        car_ins_num: '123456',
        car_creater: 'kinmin'
      },
      {
        car_num: '12987133',
        car_model_id: '123',
        car_color: '红色',
        car_engine_num: '45432',
        car_frame_num: '47186',
        car_buy_date: '2016-2-3',
        car_retailer: '10333',
        car_status: '已租',
        car_ins_num: '123456',
        car_creater: 'kinmin'
      },
      {
        car_num: '12987134',
        car_model_id: '123',
        car_color: '红色',
        car_engine_num: '45432',
        car_frame_num: '47186',
        car_buy_date: '2016-2-3',
        car_retailer: '10333',
        car_status: '已租',
        car_ins_num: '123456',
        car_creater: 'kinmin'
      },
      {
        car_num: '12987135',
        car_model_id: '123',
        car_color: '红色',
        car_engine_num: '45432',
        car_frame_num: '47186',
        car_buy_date: '2016-2-3',
        car_retailer: '10333',
        car_status: '已租',
        car_ins_num: '123456',
        car_creater: 'kinmin'
      }
      ]
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
