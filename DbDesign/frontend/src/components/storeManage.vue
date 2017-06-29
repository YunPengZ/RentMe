<template>
<div>
    <!--门店信息管理-->
<el-row type="flex" class="firstRow">
<el-autocomplete
  popper-class="my-autocomplete"
  v-model="state3"
  :fetch-suggestions="querySearch"
  custom-item="my-item-zh"
  placeholder="搜索门店"
  @select="handleSelect"
  icon="edit"
  :on-icon-click="handleIconClick"
>
</el-autocomplete>
<router-link :to="'/home/addCar'"  class="rid">
<el-button type="primary" icon="edit" class="addButton">添加门店信息</el-button>
</router-link>
</el-row>
<el-row type="flex" class="secondRow">
<el-col :offset="4" :span="16">
  <el-table
    :data="tableStore"
    height="250"
    style="width: 100%">
    <el-table-column
      type="index"
      >
    </el-table-column>
    <el-table-column
      label="门店地址"
      prop="store_addr">
    </el-table-column>
    <el-table-column
      label="门店联系方式"
      prop="store_tel">
    </el-table-column>
    <el-table-column
      label="门店营业时间"
      prop="store_start_time">
    </el-table-column>
    <el-table-column
      label="门店管理员"
      prop="store_admin">
    </el-table-column>

        <el-table-column
      label="操作"
      prop="desc"
      >
            <template scope="props">
                <router-link :to="'/home/editStore/'+props.row.store_id"  class="rid">
        <el-button
          size="small">            
          
              编辑
            
            </el-button>
            </router-link>

        <el-button
          size="small"
          type="danger"
          @click="deleteStore(props.row.store_id)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</el-col>
</el-row>

<!--门店管理员信息管理-->

<el-row type="flex" class="firstRow">
<el-autocomplete
  popper-class="my-autocomplete"
  v-model="state3"
  :fetch-suggestions="querySearch"
  custom-item="my-item-zh"
  placeholder="搜索门店管理员"
  @select="handleSelect"
  icon="edit"
  :on-icon-click="handleIconClick"
>
</el-autocomplete>
<router-link :to="'/home/addStore'"  class="rid">
<el-button type="primary" icon="edit" class="addButton">添加门店管理员信息</el-button>
</router-link>
</el-row>
<el-row type="flex" class="secondRow">
<el-col :offset="4" :span="16">
  <el-table
    :data="tableManager"
    height="250"
    border
    style="width: 100%">
    <el-table-column
    fixed
      type="index"
      width="50"
      >
    </el-table-column>
    <el-table-column
      width="100"
      label="姓名"
      prop="admin_name">
    </el-table-column>
    <el-table-column
    width="100"
      label="性别"
      prop="admin_sex">
    </el-table-column>
    <el-table-column
    width="100"
      label="年龄"
      prop="admin_age">
    </el-table-column>
    <el-table-column
    width="200"
      label="身份证"
      prop="admin_ident">
    </el-table-column>
        <el-table-column
        width="200"
      label="电话"
      prop="admin_tel">
    </el-table-column>
        <el-table-column
        width="200"
      label="EMAIL"
      prop="admin_email">
    </el-table-column>
        <el-table-column
        width="200"
      label="管理员类型"
      prop="admin_type">
    </el-table-column>

        <el-table-column
        width="150"
      label="操作"
      prop="desc"
      fixed="right"
      >
            <template scope="props">
                <router-link :to="'/home/editManager/'+props.row.admin_id"  class="rid">
        <el-button
          size="small">            
          
              编辑
            
            </el-button>
            </router-link>

        <el-button
          size="small"
          type="danger"
          @click="deleteManager(props.row.admin_id)">删除</el-button>
      </template>
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
      tableStore: [
      //   {
      //   store_addr: '12987132',
      //   store_tel: '123',
      //   store_start_time: '红色',
      //   store_admin: '45432'
      // }
      ],
      tableManager: [
      //   {
      //   admin_name: '12987132',
      //   admin_sex: '123',
      //   admin_age: '红色',
      //   admin_ident: '45432',
      //   admin_tel: '18756010918',
      //   admin_email: '2087447114@qq.com',
      //   admin_type: '大中华区管理员'
      // }

      ]
    }
  },
  created () {
    var self = this
        // var id = self.$route.params.id;
    axios.get('/test/admins', {})
         .then(function (response) {
           self.tableManager = response.data
         })
         .catch(e => {
           this.errors.push(e)
         })

    axios.get('/test/stores', {})
         .then(function (response) {
           self.tableStore = response.data
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    deleteStore (event) {
      var self = this
      // console.log(self.form.account)
      axios.post('/test/stores', {
        statu: 'delete',
        store_id: self.tableStore.store_id
      })
            .then(function (response) {
              self.$message('删除成功')
            })
            .catch(e => {
              self.$message('删除失败')
              this.errors.push(e)
            })
    },
    deleteManager (event) {
      var self = this
      // console.log(self.form.account)
      axios.delete('/test/admins', {
        statu: 'delete',
        admin_id: self.tableStore.admin_id
      })
            .then(function (response) {
              self.$message('删除成功')
            })
            .catch(e => {
              self.$message('删除失败')
              this.errors.push(e)
            })
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
