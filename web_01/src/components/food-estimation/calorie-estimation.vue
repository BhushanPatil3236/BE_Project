<template>
  <div>
    <div>
      <template>
        <v-simple-table fixed-header id="header">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left"> User Name </th>
                <th class="text-left"> Predicted Image </th>
                <th class="text-left"> sugar (gram/s)</th>
                <th class="text-left"> fiber (gram/s)</th>
                <th class="text-left"> serving_size (gram/s)</th>
                <th class="text-left"> sodium (miligram/s)</th>
                <th class="text-left"> potassium (gram/s)</th>
                <th class="text-left"> fat_saturated (gram/s)</th>
                <th class="text-left"> fat (gram/s)</th>
                <th class="text-left"> calories (gram/s)</th>
                <th class="text-left"> cholesterol (kcal)</th>
                <th class="text-left"> protein (gram/s)</th>
                <th class="text-left"> carbohydrates (gram/s)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="value in datas" :key="value.id">
                <td>{{ value.user_name }}</td>
                <td>{{ value.img_name }}</td>
                <td>{{ value.sugar }}</td>
                <td>{{ value.fiber }}</td>
                <td>{{ value.serving_size }}</td>
                <td>{{ value.sodium }}</td>
                <td>{{ value.potassium }}</td>
                <td>{{ value.fat_saturated }}</td>
                <td>{{ value.fat }}</td>
                <td>{{ value.calories }}</td>
                <td>{{ value.cholesterol }}</td>
                <td>{{ value.protein }}</td>
                <td>{{ value.carbohydrates }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </template>
    </div>

    <v-card :loading="loading" class="mx-auto my-12" max-width="374">
      <v-container class="justify-center">
        <template slot="progress">
          <v-progress-linear
            color="primary"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>

        <v-card-title class="justify-center">Calculate Calories</v-card-title>

        <v-card-text>
          <template>
            <ValidationObserver ref="observer" v-slot="{ invalid }">
              <form @submit.prevent="Login">
                <v-file-input
                  v-model="fileInput"
                  :rules="rules"
                  accept="image/png, image/jpeg, image/bmp, image/jpg"
                  placeholder="Pick an photo"
                  prepend-icon="mdi-camera"
                  label="Food Dish"
                ></v-file-input>

                <div>
                  <v-spacer></v-spacer>
                  <v-btn class="ma-4" text @click="Submit" :disabled="invalid">
                    Submit
                  </v-btn>
                </div>
              </form>
            </ValidationObserver>
          </template>
        </v-card-text>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
export default {
  data: () => ({
    fileInput: [],
    form: new FormData(),
    datas: "",
    token: Vue.$cookies.get("token"),
  }),

  mounted() {
    this.Get();
  },

  methods: {
    Submit() {
      this.$refs.observer.validate().then(success => {
        if (!success) {
          return;
        }

        this.form.append("image", this.fileInput);

        axios({
          method: "POST",
          url: "http://127.0.0.1:8000/estimate-food/",
          data:this.form,
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `token ${this.token}`,
          }
        })
          .then(res => {
            console.log(res);
            alert("Image predicted successfully!");
            window.location.reload();
          })
          .catch(error => {
            alert(error);
            this.errored = true;
          });

        this.loading = true;
        setTimeout(() => (this.loading = false), 2000);
      });
    },

    Get() {
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/estimate-food/",
        data: JSON.stringify({}),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.datas = res.data
          console.log(this.data);
        })
        .catch((error) => {
          alert(error);
          this.errored = true;
        });
    },
  }
};
</script>

<style></style>
