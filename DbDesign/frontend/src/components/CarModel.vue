<template>
  <div>
    <el-card>
      <el-row>
        <el-col :span="12">
          <el-form :model="ruleForm" label-width="50px">
            <el-form-item label="车牌">
              <el-select v-model="ruleForm.car_brand" multiple placeholder="请选择车辆品牌">
                <el-option
                  v-for="item in options['car_brand']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="车型">
              <el-select v-model="ruleForm.car_type" multiple placeholder="请选择车辆类型">
                <el-option
                  v-for="item in options['car_type']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="座位">
              <el-select v-model="ruleForm.car_seats_num" multiple placeholder="请选择座位数量">
                <el-option
                  v-for="item in options['car_seats_num']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="车门">
              <el-select v-model="ruleForm.car_doors" multiple placeholder="请选择车门数量">
                <el-option
                  v-for="item in options['car_doors']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="燃料">
              <el-select v-model="ruleForm.car_fuel_type" multiple placeholder="请选择燃料类型">
                <el-option
                  v-for="item in options['car_fuel_type']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="变速">
              <el-select v-model="ruleForm.car_gearbox_type" multiple placeholder="请选择变速箱类型">
                <el-option
                  v-for="item in options['car_gearbox_type']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="排量">
              <el-select v-model="ruleForm.car_displacement" multiple placeholder="请选择排量大小">
                <el-option
                  v-for="item in options['car_displacement']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="燃油">
              <el-select v-model="ruleForm.car_fuel_num" multiple placeholder="请选择燃油编号">
                <el-option
                  v-for="item in options['car_fuel_num']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="驱动">
              <el-select v-model="ruleForm.car_drive_way" multiple placeholder="请选择驱动方式">
                <el-option
                  v-for="item in options['car_drive_way']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="12">
          <el-form :model="ruleForm" label-width="50px">
            <el-form-item label="进气">
              <el-select v-model="ruleForm.car_engine_intake" multiple placeholder="请选择进气方式">
                <el-option
                  v-for="item in options['car_engine_intake']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="天窗">
              <el-select v-model="ruleForm.car_skylight" multiple placeholder="请选择天窗类型">
                <el-option
                  v-for="item in options['car_skylight']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="油箱">
              <el-select v-model="ruleForm.car_tank_capa" multiple placeholder="请选择油箱容量">
                <el-option
                  v-for="item in options['car_tank_capa']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="音响">
              <el-select v-model="ruleForm.car_voicebox" multiple placeholder="请选择音响数量">
                <el-option
                  v-for="item in options['car_voicebox']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="座椅">
              <el-select v-model="ruleForm.car_seats_type" multiple placeholder="请选择座椅类型">
                <el-option
                  v-for="item in options['car_seats_type']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="雷达">
              <el-select v-model="ruleForm.car_reverse_radar" multiple placeholder="请选择倒车雷达">
                <el-option
                  v-for="item in options['car_reverse_radar']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="气囊">
              <el-select v-model="ruleForm.car_airbag" multiple placeholder="请选择气囊数量">
                <el-option
                  v-for="item in options['car_airbag']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="媒体">
              <el-select v-model="ruleForm.car_dvd" multiple placeholder="请选择车载媒体">
                <el-option
                  v-for="item in options['car_dvd']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="导航">
              <el-select v-model="ruleForm.car_gps" multiple placeholder="请选择车载导航">
                <el-option
                  v-for="item in options['car_gps']"
                  :key="item"
                  :label="item"
                  :value="item">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :span="6">
          <p class="text">*不选则默认不作要求</p>
          <el-button type="primary" @click="handleSubmit()">提交</el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      options: {
        car_type: [0, 1, 2],
        car_brand: ['MINI', '江淮', '传祺', '风行', '标致', '长城', '雪铁龙', '宝利格', '三菱', '奇瑞', '宝马', '雪佛兰', 'smart', '沃尔沃', '北京汽车', '东南汽车', '起亚', '别克', '长丰', '大众', '华颂', '日产', '依维柯', '猎豹', '斯柯达', '奥迪', '上汽大通', '野马', '戴姆勒', '马自达', '比亚迪', '江铃', '本田', '丰田', '菲亚特', '福特', '奔驰', '现代', '雪铁龙DS', '铃木', '凯迪拉克', '金杯'],
        car_seats_num: ['2', '3', '4', '5', '6', '7', '8', '9'],
        car_doors: ['5', '4', '3', '0', '2'],
        car_fuel_type: ['汽油', '油电混合', '柴油'],
        car_gearbox_type: ['AMT', 'CVT', 'MT', 'AT'],
        car_displacement: ['2.0', '2384', '1298', '1498', '2953', '1599', '1975', '2438', '1490', '1591', '1798', '1781', '1598', '2968', '1499', '1999', '1396', '1497', '1584', '1969', '2362', '2694', '2359', '2497', '2997', '1796', '2494', '1390', '1984', '2360', '2700', '1206', '1399', '2354', '1597', '1997', '1360', '1751', '1595', '2996', '2521', '1995', '1596', '1349', '2260', '2975', '2185', '1372', '2351', '1329', '1197', '3498', '1590', '2672', '1784', '2388', '1485', '1587', '2998', '1339', '1998', '2488', '2496', '2253', '2995', '2.4'],
        car_fuel_num: ['92-93汽油', '其他', '95-97汽油'],
        car_drive_way: ['四驱', '其他', '后驱', '前驱'],
        car_engine_intake: ['涡轮增压', '其他', '自然吸气'],
        car_skylight: ['全景天窗', '其他', '无', '单天窗'],
        car_tank_capa: ['62', '63', '72', '42', '60', '65', '53', '66', '51', '44', '87', '64', '101', '40', '50', '138', '77', '56', '43', '92', '46', '45', '58', '54', '80', '70', '90', '73', '55', '75', '52', '33', '41'],
        car_voicebox: ['2', '12', '10', '无', '5', '6', '8', '4', '7'],
        car_seats_type: ['织物座椅', '皮革座椅', '其他'],
        car_reverse_radar: ['无', '有', '其他'],
        car_airbag: ['无', '1', '2', '8', '3', '4', '6', '7', '5'],
        car_dvd: ['DVD', 'CD', '其他', '无'],
        car_gps: ['其他', '有', '无']
      },
      ruleForm: {
        car_brand: [],
        car_type: [],
        car_seats_num: [],
        car_doors: [],
        car_fuel_type: [],
        car_gearbox_type: [],
        car_displacement: [],
        car_fuel_num: [],
        car_drive_way: [],
        car_engine_intake: [],
        car_skylight: [],
        car_tank_capa: [],
        car_voicebox: [],
        car_seats_type: [],
        car_reverse_radar: [],
        car_airbag: [],
        car_dvd: [],
        car_gps: []
      }
    }
  },
  computed: {
    form () {
      let form = this.ruleForm
      if (form['car_brand'].length === 0) {
        form['car_brand'] = this.options['car_brand']
      }
      if (form['car_type'].length === 0) {
        form['car_type'] = this.options['car_type']
      }
      if (form['car_seats_num'].length === 0) {
        form['car_seats_num'] = this.options['car_seats_num']
      }
      if (form['car_doors'].length === 0) {
        form['car_doors'] = this.options['car_doors']
      }
      if (form['car_fuel_type'].length === 0) {
        form['car_fuel_type'] = this.options['car_fuel_type']
      }
      if (form['car_gearbox_type'].length === 0) {
        form['car_gearbox_type'] = this.options['car_gearbox_type']
      }
      if (form['car_displacement'].length === 0) {
        form['car_displacement'] = this.options['car_displacement']
      }
      if (form['car_fuel_num'].length === 0) {
        form['car_fuel_num'] = this.options['car_fuel_num']
      }
      if (form['car_drive_way'].length === 0) {
        form['car_drive_way'] = this.options['car_drive_way']
      }
      if (form['car_engine_intake'].length === 0) {
        form['car_engine_intake'] = this.options['car_engine_intake']
      }
      if (form['car_skylight'].length === 0) {
        form['car_skylight'] = this.options['car_skylight']
      }
      if (form['car_tank_capa'].length === 0) {
        form['car_tank_capa'] = this.options['car_tank_capa']
      }
      if (form['car_voicebox'].length === 0) {
        form['car_voicebox'] = this.options['car_voicebox']
      }
      if (form['car_seats_type'].length === 0) {
        form['car_seats_type'] = this.options['car_seats_type']
      }
      if (form['car_reverse_radar'].length === 0) {
        form['car_reverse_radar'] = this.options['car_reverse_radar']
      }
      if (form['car_airbag'].length === 0) {
        form['car_airbag'] = this.options['car_airbag']
      }
      if (form['car_dvd'].length === 0) {
        form['car_dvd'] = this.options['car_dvd']
      }
      if (form['car_gps'].length === 0) {
        form['car_gps'] = this.options['car_gps']
      }
      return form
    }
  },
  methods: {
    handleSubmit () {
      var self = this
      axios.post('/test/findcar/', {
        car_brand: self.form.car_brand,
        car_type: self.form.car_type,
        car_seats_num: self.form.car_seats_num,
        car_doors: self.form.car_doors,
        car_fuel_type: self.form.car_fuel_type,
        car_gearbox_type: self.form.car_gearbox_type,
        car_displacement: self.form.car_displacement,
        car_fuel_num: self.form.car_fuel_num,
        car_drive_way: self.form.car_drive_way,
        car_engine_intake: self.form.car_engine_intake,
        car_skylight: self.form.car_skylight,
        car_tank_capa: self.form.car_tank_capa,
        car_voicebox: self.form.car_voicebox,
        car_seats_type: self.form.car_seats_type,
        car_reverse_radar: self.form.car_reverse_radar,
        car_airbag: self.form.car_airbag,
        car_dvd: self.form.car_dvd,
        car_gps: self.form.car_gps
      }).then(function (response) {
        self.$message('车型选择成功')
        self.$store.state.matched_car = response.data
        self.$store.state.step = 2
        self.$router.push('/home/new_order/car_choose')
        self.$router.go(1)
      }).catch(e => {
        self.$message('选择失败')
        this.errors.push(e)
      })
    },
    handleCheckAllChange (event) {
    },
    handleCheckedCitiesChange (value) {
      let checkedCount = value.length
      this.checkAll = checkedCount === this.options['car_type'].length
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.options['car_type'].length
    }
  }
}
</script>
<style scoped>
.text{
  font-size: 5px;
  color:grey;
}
</style>
