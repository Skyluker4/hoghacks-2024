// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'formation.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Formation _$FormationFromJson(Map<String, dynamic> json) => Formation(
      image: json['image'] as String,
      name: json['name'] as String,
      weight: (json['weight'] as num).toDouble(),
    );

Map<String, dynamic> _$FormationToJson(Formation instance) => <String, dynamic>{
      'image': instance.image,
      'name': instance.name,
      'weight': instance.weight,
    };
