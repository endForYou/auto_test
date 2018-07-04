# coding=utf8
import xlwt
import xlrd
import time
import os
from xlutils.copy import copy

# 定义业务类型
TYPE_OF_FIVE = 1  # 五险一金
TYPE_OF_ALONE = 2  # 独立户
TYPE_OF_OTHER = 3  # 其它业务


class createXrdFile(object):
    def createAddMemberRecord(
            self,
            fileName,
            name,
            date_str,
            card_numbers_str,
            client="",
            business_type=TYPE_OF_FIVE,
            hf_date_str="",
            is_other=False):
        """
        创建增员excel
        :param fileName:
        :param name:
        :param date_str:
        :param client:
        :param card_numbers_str:
        :param business_type:
        :return:
        """
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        if business_type == TYPE_OF_FIVE:
            business_type_name = u"人事代理-标准"
        elif business_type == TYPE_OF_ALONE:
            business_type_name = u"独立户"
        else:
            business_type_name = u"代发工资"

        card_numbers_list = card_numbers_str.split(',')
        record_number = len(card_numbers_list)

        for x in range(1, record_number + 1):
            sheet.write(x, 0, name.decode("utf8") + str(x))
            sheet.write(x, 1, "身份证".decode("utf8"))
            sheet.write(x, 2, card_numbers_list[x - 1])
            sheet.write(x, 3, "非本地城镇".decode("utf8"))
            sheet.write(x, 4, "18607132781".decode("utf8"))
            sheet.write(x, 5, business_type_name)
            if business_type == TYPE_OF_FIVE:
                sheet.write(x, 6, "10000")
                sheet.write(x, 7, "20000")
                sheet.write(x, 8, "10")
                sheet.write(x, 9, "20")
                sheet.write(x, 10, "江苏南京市".decode("utf8"))
                sheet.write(x, 11, client.decode("utf8"))
                sheet.write(x, 12, date_str)
                if not is_other:
                    if hf_date_str:
                        sheet.write(x, 13, hf_date_str)
                    else:
                        sheet.write(x, 13, date_str)
            else:
                sheet.write(x, 6, "江苏南京市".decode("utf8"))
                sheet.write(x, 7, client.decode("utf8"))
                sheet.write(x, 8, date_str)
                if not is_other:
                    if hf_date_str:
                        sheet.write(x, 9, hf_date_str)
                    else:
                        sheet.write(x, 9, date_str)
        new_wb.save(fileName)
        return card_numbers_list

    def createReduceMemberRecord(
            self,
            fileName,
            name,
            date_str,
            card_numbers_str,
            client,
            business_type=TYPE_OF_FIVE):
        """
        创建减员excel
        :param fileName:
        :param name:
        :param client:
        :param date_str:
        :param card_numbers_str:
        :param business_type:
        :return:
        """
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        # 减员类型赋值
        if business_type == TYPE_OF_FIVE:
            business_type_name = u"人事代理-标准"
        elif business_type == TYPE_OF_ALONE:
            business_type_name = u"独立户"
        else:
            business_type_name = u"代发工资"
        card_numbers_list = card_numbers_str.split(',')
        record_number = len(card_numbers_list)
        for x in range(1, record_number + 1):
            sheet.write(x, 0, name.decode("utf8") + str(x))
            sheet.write(x, 1, "身份证".decode("utf8"))
            sheet.write(x, 2, card_numbers_list[x - 1])
            sheet.write(x, 3, "非本地城镇".decode("utf8"))
            sheet.write(x, 4, "18607132781".decode("utf8"))
            sheet.write(x, 5, business_type_name)
            sheet.write(x, 6, "江苏南京市".decode("utf8"))
            sheet.write(x, 7, client.decode("utf8"))
            sheet.write(x, 8, date_str)
        new_wb.save(fileName)
        return card_numbers_list

    def createOffsetMemberRecord(
            self,
            fileName,
            name,
            date_str,
            card_numbers_str,
            client,
            business_type=TYPE_OF_FIVE,
            hf_date_str=""):
        """
        创建补缴excel
        :param fileName:
        :param name:
        :param client:
        :param date_str:
        :param card_numbers_str:
        :param business_type:
        :return:
        """
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        if business_type == TYPE_OF_FIVE:
            business_type_name = u"人事代理-标准"
        else:
            business_type_name = u"独立户"
        card_numbers_list = card_numbers_str.split(',')
        record_number = len(card_numbers_list)
        for x in range(1, record_number + 1):
            sheet.write(x, 0, name.decode("utf8") + str(x))
            sheet.write(x, 1, "身份证".decode("utf8"))
            sheet.write(x, 2, card_numbers_list[x - 1])
            sheet.write(x, 3, "非本地城镇".decode("utf8"))
            sheet.write(x, 4, "18607132781".decode("utf8"))
            sheet.write(x, 5, business_type_name)
            if business_type == TYPE_OF_FIVE:
                sheet.write(x, 6, "10000")
                sheet.write(x, 7, "20000")
                sheet.write(x, 8, "10")
                sheet.write(x, 9, "20")
                sheet.write(x, 10, "江苏南京市".decode("utf8"))
                sheet.write(x, 11, client.decode("utf8"))
                sheet.write(x, 12, date_str)
                sheet.write(x, 13, date_str)
                if hf_date_str:
                    sheet.write(x, 14, hf_date_str)
                else:
                    sheet.write(x, 14, date_str)
            else:
                sheet.write(x, 6, "江苏南京市".decode("utf8"))
                sheet.write(x, 7, client.decode("utf8"))
                sheet.write(x, 8, date_str)
                sheet.write(x, 9, date_str)
                if hf_date_str:
                    sheet.write(x, 10, hf_date_str)
                else:
                    sheet.write(x, 10, date_str)
        new_wb.save(fileName)
        return card_numbers_list

    def createPolicyBagInformation(
            self,
            fileName,
            name,
            attendPlace=u"江苏南京市",
            effectDay="2017-07-26",
            fromWhere=u"自建",
            isDefault=u"是",
            need_change_number=0,
            polciybag_type="supplier"):
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        if not 0 <= int(need_change_number) < 9:
            need_change_number = 9
        name_list = name.split(',')
        record_number = len(name_list)
        for x in range(2, record_number + 2):
            sheet.write(x, 0, name_list[x - 2])
            sheet.write(x, 1, attendPlace.decode("utf8"))
            sheet.write(x, 2, effectDay.decode("utf8"))
            sheet.write(x, 3, fromWhere.decode("utf8"))
            if polciybag_type == "supplier":
                sheet.write(x, 4, isDefault.decode("utf8"))
                for c in range(5, 78, 9):
                    sheet.write(x, c, 10)
                for c in range(6, 79, 9):
                    sheet.write(x, c, 10)
                for c in range(7, 80, 9):
                    sheet.write(x, c, 10)
                for c in range(8, 81, 9):
                    sheet.write(x, c, 10)
                for c in range(9, 82, 9):
                    sheet.write(x, c, 10)
                for c in range(10, 83, 9):
                    sheet.write(x, c, 10)
                for c in range(11 + 9 * need_change_number, 84, 9):
                    sheet.write(x, c, u"四舍五入")
                for c in range(12 + 9 * need_change_number, 85, 9):
                    sheet.write(x, c, u"两位")
                for c in range(13 + 9 * need_change_number, 86, 9):
                    sheet.write(x, c, u"是")
                for c in range(11, 11 + 9 * (need_change_number - 1) + 1, 9):
                    if c % 2 == 0:
                        sheet.write(x, c, u"强行截位")
                    else:
                        sheet.write(x, c, u"强行进位")
                for c in range(12, 12 + 9 * (need_change_number - 1) + 1, 9):
                    if c % 2 == 0:
                        sheet.write(x, c, u"整数")
                    else:
                        sheet.write(x, c, u"一位")
                for c in range(13, 13 + 9 * (need_change_number - 1) + 1, 9):
                    sheet.write(x, c, u"否")
            else:
                for c in range(4, 77, 9):
                    sheet.write(x, c, 10)
                for c in range(5, 78, 9):
                    sheet.write(x, c, 10)
                for c in range(6, 79, 9):
                    sheet.write(x, c, 10)
                for c in range(7, 80, 9):
                    sheet.write(x, c, 10)
                for c in range(8, 81, 9):
                    sheet.write(x, c, 10)
                for c in range(9, 82, 9):
                    sheet.write(x, c, 10)
                for c in range(10 + 9 * need_change_number, 84, 9):
                    sheet.write(x, c, u"四舍五入")
                for c in range(11 + 9 * need_change_number, 85, 9):
                    sheet.write(x, c, u"两位")
                for c in range(12 + 9 * need_change_number, 86, 9):
                    sheet.write(x, c, u"是")
                for c in range(10, 10 + 9 * (need_change_number - 1) + 1, 9):
                    if c % 2 == 0:
                        sheet.write(x, c, u"强行截位")
                    else:
                        sheet.write(x, c, u"强行进位")
                for c in range(11, 11 + 9 * (need_change_number - 1) + 1, 9):
                    if c % 2 == 0:
                        sheet.write(x, c, u"整数")
                    else:
                        sheet.write(x, c, u"一位")
                for c in range(12, 12 + 9 * (need_change_number - 1) + 1, 9):
                    sheet.write(x, c, u"否")
        new_wb.save(fileName)
        return True

    def createPolicyBagDetail(
            self,
            fileName,
            need_change_number=0):
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        if not 0 <= int(need_change_number) < 9:
            need_change_number = 9
        for i in range(1, 10):
            for x in range(1, 7):
                sheet.write(i, x, 10.01)
        for c in range(need_change_number + 1, 10):
            sheet.write(c, 7, u"四舍五入")
        for c in range(need_change_number + 1, 10):
            sheet.write(c, 8, u"两位")
        for c in range(need_change_number + 1, 10):
            sheet.write(c, 9, u"是")
        for c in range(1, need_change_number + 10):
            if c % 2 == 0:
                sheet.write(c, 7, u"强行截位")
            else:
                sheet.write(c, 7, u"强行进位")
        for c in range(1, need_change_number + 1):
            if c % 2 == 0:
                sheet.write(c, 8, u"整数")
            else:
                sheet.write(c, 8, u"一位")
        for c in range(1, need_change_number + 1):
            sheet.write(c, 9, u"否")
        new_wb.save(fileName)
        return fileName

    def createRealDoImport(
            self,
            fileName,
            si_status="",
            hf_status="",
            verify_all=True,
    ):
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        si_status_list = [u"确认实做", u"下月实做", u"无法缴纳", u"下月补本月", u"实做中"]
        hf_status_list = [u"确认实做", u"下月实做", u"无法缴纳", u"下月补本月", u"实做中"]
        result_list = []
        if verify_all:
            for i in range(0, 5):
                for j in range(0, 5):
                    sheet.write(i * 5 + j + 2, 19, si_status_list[i])
                    sheet.write(i * 5 + j + 2, 20, hf_status_list[j])
                    if si_status_list[i] == u"确认实做":
                        if hf_status_list[j] in (u"确认实做", u"无法缴纳"):
                            result_list.append(u"确认实做")
                        else:
                            result_list.append(u"部分实做")
                    elif si_status_list[i] == u"下月实做":
                        if hf_status_list[j] in (u"确认实做", u"无法缴纳", u"下月补本月"):
                            result_list.append(u"部分实做")
                        else:
                            result_list.append(u"实做中")
                    elif si_status_list[i] == u"无法缴纳":
                        if hf_status_list[j] == u"确认实做":
                            result_list.append(u"确认实做")
                        elif hf_status_list[j] == u"无法缴纳":
                            result_list.append(u"无法缴纳")
                        else:
                            result_list.append(u"部分实做")
                    elif si_status_list[i] == u"下月补本月":
                        result_list.append(u"部分实做")
                    elif si_status_list[i] == u"实做中":
                        if hf_status_list[j] in(u"实做中",u"下月实做") :
                            result_list.append(u"实做中")
                        else:
                            result_list.append(u"部分实做")
            for i in range(2, 27):
                for c in range(23, 112):
                    sheet.write(i, c, i * 10)
                for c in range(22, 103, 10):
                    sheet.write(i, c, u"江苏南京市")
        else:
            sheet.write(
                2, 19, si_status) if si_status else sheet.write(
                    2, 19, si_status_list[0])
            sheet.write(
                2, 20, hf_status) if hf_status else sheet.write(
                    2, 19, hf_status_list[0])
        new_wb.save(fileName)
        return result_list

    def createRealDoImport(
            self,
            fileName,
            si_status="",
            hf_status="",
            verify_all=True,
    ):
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        si_status_list = [u"确认实做", u"下月实做", u"无法缴纳", u"下月补本月", u"实做中"]
        hf_status_list = [u"确认实做", u"下月实做", u"无法缴纳", u"下月补本月", u"实做中"]
        result_list = []
        if verify_all:
            for i in range(0, 5):
                for j in range(0, 5):
                    sheet.write(i * 5 + j + 2, 19, si_status_list[i])
                    sheet.write(i * 5 + j + 2, 20, hf_status_list[j])
                    if si_status_list[i] == u"确认实做":
                        if hf_status_list[j] in (u"确认实做", u"无法缴纳"):
                            result_list.append(u"确认实做")
                        else:
                            result_list.append(u"部分实做")
                    elif si_status_list[i] == u"下月实做":
                        if hf_status_list[j] in (u"确认实做", u"无法缴纳", u"下月补本月"):
                            result_list.append(u"部分实做")
                        else:
                            result_list.append(u"实做中")
                    elif si_status_list[i] == u"无法缴纳":
                        if hf_status_list[j] == u"确认实做":
                            result_list.append(u"确认实做")
                        elif hf_status_list[j] == u"无法缴纳":
                            result_list.append(u"无法缴纳")
                        else:
                            result_list.append(u"部分实做")
                    elif si_status_list[i] == u"下月补本月":
                        result_list.append(u"部分实做")
                    elif si_status_list[i] == u"实做中":
                        if hf_status_list[j] in(u"实做中",u"下月实做") :
                            result_list.append(u"实做中")
                        else:
                            result_list.append(u"部分实做")
            for i in range(2, 27):
                for c in range(23, 112):
                    sheet.write(i, c, i * 10)
                for c in range(22, 103, 10):
                    sheet.write(i, c, u"江苏南京市")
        else:
            sheet.write(
                2, 19, si_status) if si_status else sheet.write(
                    2, 19, si_status_list[0])
            sheet.write(
                2, 20, hf_status) if hf_status else sheet.write(
                    2, 19, hf_status_list[0])
        new_wb.save(fileName)
        return result_list

    def createCastDownRealDoImport(
            self,
            fileName,
            si_status="",
            verify_all=True,
    ):
        old_wb = xlrd.open_workbook(fileName, formatting_info=True)
        new_wb = copy(old_wb)
        sheet = new_wb.get_sheet(0)
        si_status_list = [u"确认实做", u"无法缴纳", u"下月补本月", u"实做中"]

        result_list = []
        if verify_all:
            for i in range(0, 4):
                sheet.write(i+2, 19, si_status_list[i])
                sheet.write(i+2, 20, si_status_list[i])

                if si_status_list[i] in (u"确认实做", u"无法缴纳", u"下月补本月"):
                    result_list.append(u"部分实做")
                else:
                    result_list.append(u"实做中")
            for i in range(2, 6):
                for c in range(23, 112):
                    sheet.write(i, c, i * 10)
                for c in range(22, 103, 10):
                    sheet.write(i, c, u"江苏南京市")
        else:
            if si_status:
                sheet.write(2, 19, si_status)
                sheet.write(2, 20, si_status)
            else:
                sheet.write(2, 19, si_status_list[0])
                sheet.write(2, 20, si_status_list[0])
        new_wb.save(fileName)
        return result_list


if __name__ == "__main__":
    pass
