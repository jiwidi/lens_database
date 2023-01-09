<script setup>

</script>
<template>
  <div class="app-wrapper">
    <div class="sidebar">
      <h1>Lens Database</h1>
      <button @click="runSql('SELECT * FROM lenses')">
        SELECT * FROM mytable
      </button>
      <h2>Filter by Name:</h2>
      <input class="form-control" />
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
      <table>
        <tr>
          <th>Name</th>
          <th>Mount</th>
          <th>Type</th>
          <th>Max aperture</th>
        </tr>
        <tr v-for="lens in result" :key="lens.name">
          <td>{{ lens.name }}</td>
          <td>{{ lens.mount }}</td>
          <td>{{ lens.type }}</td>
          <td>F/{{ lens.max_aperture }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import FilterButton from './components/FilterButton.vue'
import { createDbWorker } from "sql.js-httpvfs"

const publicPath = "/"
const workerUrl = new URL(
  "sql.js-httpvfs/dist/sqlite.worker.js",
  import.meta.url,
);
const wasmUrl = new URL(
  "sql.js-httpvfs/dist/sql-wasm.wasm",
  import.meta.url,
);

export default {
  name: "main",
  data() {
    return {
      result: null,
      apertures: null,
    }
  },

  async mounted () {
    this.worker = await createDbWorker(
      [
        {
          from: "inline",
          config: {
            serverMode: "full",
            url: `${publicPath}db/lenses.db`,
            requestChunkSize: 4096,
          },
        },
      ],
      workerUrl.toString(),
      wasmUrl.toString()
    )

    await this.runSql('SELECT * FROM lenses')
    this.apertures = [...new Set(this.result.map(lens => lens.max_aperture))]
  },

  methods: {
    pishita (field, value, action) {
      //runSql() con la query que toque
      //update result
      //ahora mismo filterButton solo gestiona si el filtro esta activo o no (action add/remove)
      //se puede usar eso para hacer pop de la string??
    },

    async runSql(sql) {
      this.result = await this.worker.db.query(sql)
      console.log(this.result)
    },
  },

  components: {
    FilterButton,
  }
}
</script>

<style scoped></style>
