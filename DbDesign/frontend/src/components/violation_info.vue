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
    <el-col :offset="4" :span="16">
<el-form :inline="true"   >
  <el-form-item >
      <el-input placeholder="请输入内容" v-model="formInline.millegal_car_num" >
    <template slot="prepend">车牌号码</template>
  </el-input>
  </el-form-item>

  <el-form-item >
      <!--<el-input placeholder="请输入内容" v-model="formInline.user" type="date">-->
    <el-date-picker
      v-model="formInline.illegal_date"
      type="date"
      placeholder="违章时间"
      :picker-options="pickerOptions0">
    </el-date-picker>
  
  </el-form-item>
</el-form>
</el-col>
    <el-col :offset="4" :span="16">
<el-form :inline="true"   >
  </el-form-item>
  <el-form-item >
      <el-input placeholder="请输入内容" v-model="formInline.illegal_bill">
    <template slot="prepend">违章金额</template>
  </el-input>
  </el-form-item>
   <el-form-item >
      <el-input placeholder="请输入内容" v-model="formInline.illegal_info">
    <template slot="prepend">违章信息</template>
  </el-input>
  </el-form-item>
   </el-form-item>
  <el-form-item >
    <el-button type="primary" @click="onSubmit">提交</el-button>

  </el-form-item>
</el-form>
</el-col>
</el-row>
<el-row type="flex">
<el-col :offset="4" :span="17">
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
import axios from 'axios'
export default {
  data () {
    return {
      table: [
        // {
        //   millegal_car_num: 'fuckyou',
        //   illegal_date: '234',
        //   illegal_bill: '1001000$',
        //   illegal_info: 'xyz'
        // },
        // {
        //   millegal_car_num: 'fuckyou-1',
        //   illegal_date: '234',
        //   illegal_bill: '1001000$',
        //   illegal_info: 'xyz'
        // }
      ],
      formInline: {
        millegal_car_num: '',
        illegal_date: '',
        illegal_bill: '',
        illegal_info: ''
      },
      displayStatus: false
    }
  },
  created () {
    var self = this
        // var id = self.$route.params.id;
    axios.get('/test/illegal', {})
         .then(function (response) {
           self.table = response.data
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    addCar () {
      var self = this
      axios.post('/test/illegal_record/', {
        status: 'add',
        millegal_car_num: self.formInline.millegal_car_num,
        illegal_date: self.formInline.illegal_date,
        illegal_bill: self.formInline.illegal_bill,
        illegal_info: self.formInline.illegal_info
      })
            .then(function (response) {
              self.$message('添加成功')
            })
            .catch(e => {
              self.$message('添加失败')
              this.errors.push(e)
            })
    }
  }
}
</script>
<style scoped>
  .firstRow {
    margin-top: 40px;
  }
  .button {
    width: 100%;
  }
</style>
