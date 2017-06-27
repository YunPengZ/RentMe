<template>
  <div class="maxheight">
    <el-row class="maxheight">
      <el-col :span="4" class="maxheight">
        <el-menu mode="vertical" default-active="1" class="maxheight">
          <el-menu-item index="1"><i class="el-icon-message"></i>导航一</el-menu-item>
          <el-menu-item index="2"><i class="el-icon-message"></i>导航二</el-menu-item>
          <el-menu-item index="3"><i class="el-icon-message"></i>导航三</el-menu-item>
          <el-menu-item index="4"><i class="el-icon-message"></i>导航四</el-menu-item>
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
  .background{
    background-color: #d1dbe5;
  }
</style>
