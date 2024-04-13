import 'package:dio/dio.dart';
import 'package:native_dio_adapter/native_dio_adapter.dart';

import 'package:playpredict/models/formation.dart';
import 'package:playpredict/models/prediction.dart';
import 'package:playpredict/models/situation.dart';

class API {
  static const String url = 'http://172.20.10.2:5500/';

  static Future<List<Formation>> getFormations() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    List<Formation> formations = [];

    try {
      final response = await dio.get('${url}api/v1/situation');
      for (var formation in response.data) {
        formations.add(Formation.fromJson(formation));
      }
    } catch (e) {
      print(e);
    }
    return formations;
  }

  static Future<List<Prediction>> getPredictions() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    List<Prediction> predictions = [];

    try {
      final response = await dio.get('${url}api/v1/situation');
      for (var prediction in response.data) {
        predictions.add(Prediction.fromJson(prediction));
      }
    } catch (e) {
      print(e);
    }
    return predictions;
  }

  static Future<Situation?> getSituation() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    Situation? situation;

    try {
      final response = await dio.get('${url}api/v1/situation');
      situation = Situation.fromJson(response.data);
    } catch (e) {
      print(e);
    }
    return situation;
  }

  static Future<void> postReset() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    await dio.post('${url}api/v1/reset');
  }
}
