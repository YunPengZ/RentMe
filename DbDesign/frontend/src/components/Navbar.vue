<template>
  <el-menu theme="dark" :default-active="'1'" mode="horizontal">
    <el-row type="flex" align="middle" justify="space-between">
      <el-col :span="12">
        <el-menu-item index="1"><img src="../assets/logo.png" width="45" height="45"></el-menu-item>
      </el-col>
      <el-col :span="12">
        <el-menu-item index="3"  style="float: right;">注销</el-menu-item>
        <el-menu-item index="2"  style="float: right;">{{ $store.state.user_Name }}</el-menu-item>
      </el-col>
    </el-row>
  </el-menu>
</template>
<script>
</script>
<style scoped>
  div{
    height: 50px;
    width: 100%;
  }
</style>
