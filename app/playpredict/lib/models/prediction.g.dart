// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'prediction.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Prediction _$PredictionFromJson(Map<String, dynamic> json) => Prediction(
      formation: json['formation'] as String,
      image: json['image'] as String,
      name: json['name'] as String,
      weight: (json['weight'] as num).toDouble(),
    );

Map<String, dynamic> _$PredictionToJson(Prediction instance) =>
    <String, dynamic>{
      'formation': instance.formation,
      'image': instance.image,
      'name': instance.name,
      'weight': instance.weight,
    };
