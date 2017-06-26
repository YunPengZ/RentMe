<template>
  <el-menu theme="dark" :default-active="1" mode="horizontal">
    <el-row type="flex" justify="space-between">
      <el-col :span="2">
        <el-menu-item index="1">LOGO</el-menu-item>
      </el-col>
      <el-col :span="2" :offset="18">
        <el-menu-item index="2">{{ $store.state.user_Name }}</el-menu-item>
        <el-menu-item index="3">注销</el-menu-item>
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
