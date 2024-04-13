import 'package:dio/dio.dart';
import 'package:native_dio_adapter/native_dio_adapter.dart';

import 'package:playpredict/models/situation.dart';

class API {
  static const String url = 'http://172.20.10.2:5500/';

  static Future<void> getFormations() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    final response = await dio.get('${url}api/v1/formations');
    print(response.data);
  }

  static Future<void> getPredictions() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    final response = await dio.get('${url}api/v1/predictions');
    print(response.data);
  }

  static Future<dynamic> getSituation() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    Situation? situation;

    try {
      final response = await dio.get('${url}api/v1/situation',
          options: Options(
            contentType: Headers.jsonContentType,
          ));
      situation = Situation.fromJson(response.data);
    } catch (e) {
      print(e);
    }
    return situation;
  }

  static Future<void> postReset() async {
    final dio = Dio();
    dio.httpClientAdapter = NativeAdapter();
    final response = await dio.post('${url}api/v1/reset');
    print(response.data);
  }
}
