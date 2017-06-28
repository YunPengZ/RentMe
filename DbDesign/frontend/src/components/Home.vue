<template>
  <div class="maxheight">
    <el-row class="maxheight">
      <el-col :span="4" class="maxheight">
        <el-menu mode="vertical" default-active="1" class="maxheight">
          <template>
            <router-link :to="'/home'" class="text">
                <el-menu-item index="1" >首页</el-menu-item>
              </router-link>
          </template>
          <template v-if="$store.state.user_Status === '门店管理员'">
            <el-menu-item-group title="订单信息">
              <router-link :to="'/home/new_order'" class="text">
                <el-menu-item index="2" >添加订单</el-menu-item>
              </router-link>
              <router-link :to="'/home/order'" class="text">
                <el-menu-item index="3" >订单管理</el-menu-item>
              </router-link>
            </el-menu-item-group>
            <el-menu-item-group title="车辆信息">
              <router-link :to="'/home/addCar'" class="text">
                <el-menu-item index="4" >添加车辆</el-menu-item>
              </router-link>
              <router-link :to="'/home/carManage'" class="text">
                <el-menu-item index="5" >车辆管理</el-menu-item>
              </router-link>
            </el-menu-item-group>
          </template>
          <template v-if="$store.state.user_Status === '违章信息管理员'">
            <el-menu-item-group title="违章信息">
              <router-link :to="'/home/violation_info'" class="text">
                <el-menu-item index="2" >违章录入</el-menu-item>
              </router-link>
            </el-menu-item-group>
          </template>
          <template v-if="$store.state.user_Status === '大中华区管理员'">
            <el-menu-item-group title="总览">
              <router-link :to="'/home/analysis'" class="text">
                <el-menu-item index="2" >统计信息</el-menu-item>
              </router-link>
            </el-menu-item-group>
            <el-menu-item-group title="管理">
              <router-link :to="'/home/storeManage'" class="text">
                <el-menu-item index="3" >门店及管理员</el-menu-item>
              </router-link>
              <router-link :to="'/home/addManager'" class="text">
                <el-menu-item index="4" >添加管理员</el-menu-item>
              </router-link>
              <router-link :to="'/home/addStore'" class="text">
                <el-menu-item index="5" >添加门店</el-menu-item>
              </router-link>
            </el-menu-item-group>
          </template>
        </el-menu>
      </el-col>
      <el-col :span="20" class="maxheight background">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  export default {
    methods: {
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
<style scoped>
  .text{
    text-decoration: none;
  }
  .background{
    background-color: #d1dbe5;
  }
</style>
