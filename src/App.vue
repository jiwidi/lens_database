<script setup>

</script>
<template>
  <div class="app-wrapper">
    <div class="sidebar">
      <h1>Lens Database</h1>
      <h2>Filter by Name:</h2>
      <input class="form-control" v-model="filters.name.value" />
      <h2>Type</h2>
      <div class="button-group">
        <FilterButton @update-filter="(action) => pishita('type', 'Zoom', action)">Zoom</FilterButton>
        <FilterButton @update-filter="(action) => pishita('type', 'Prime', action)">Prime</FilterButton>
      </div>
      <h2>Aperture</h2>
      <div class="button-group">
        <FilterButton v-for="aperture in apertures" :key="aperture" @update-filter="(action) => pishita('aperture', aperture, action)">{{ aperture }}</FilterButton>
      </div>
    </div>
    <div class="content">
      <VTable :data="lenses" :filters="filters">
        <template #head>
          <tr>
            <th>Name</th>
            <th>Mount</th>
            <th>Type</th>
            <th>Max aperture</th>
            <th>Ø filter</th>
          </tr>
        </template>
        <template #body="{ rows }">
          <tr v-for="row in rows" :key="row.name">
            <td>{{ row.name }}</td>
            <td>{{ row.mount }}</td>
            <td>{{ row.type }}</td>
            <td>{{ row.maxAperture }}</td>
            <td>{{ row.filterSize }}</td>
          </tr>
        </template>
      </VTable>
    </div>
  </div>
</template>

<script>
import lenses from './data/lenses.json'
import FilterButton from './components/FilterButton.vue'

export default {
  name: "main",
  data() {
    return {
      lenses,
      apertures: null,
      filters: {
        name: { value: "", keys: ["name"] },
        type: { value: [], custom: this.typeFilter },
        aperture: { value: [], custom: this.apertureFilter }
      }
    }
  },

  mounted () {
    this.apertures = [...new Set(this.lenses.map(lens => lens.maxAperture))]
  },

  methods: {
    typeFilter (filterValue, row) {
      if (filterValue.length === 0) return true
      else return filterValue.includes(row.type)
    },

    apertureFilter (filterValue, row) {
      if (filterValue.length === 0) return true
      else return filterValue.includes(row.maxAperture)
    },

    pishita (field, value, action) {
      action === 'add' ? this.filters[field].value.push(value) : this.filters[field].value.pop(value)
    }
  },

  components: {
    FilterButton,
  }
}
</script>

<style scoped></style>
